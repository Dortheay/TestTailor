import os
import re
import ast
from collections import defaultdict
from typing import Dict, List, Set, Tuple


class ImportGenerator:
    def __init__(self, test_folder_path: str):
        """
        初始化 ImportGenerator 类
        
        Args:
            test_folder_path: 测试文件夹的路径
        """
        self.test_folder_path = test_folder_path
        self.import_statements = set()  # 存储最终的 import 语句
        self.module_aliases = defaultdict(set)  # 存储模块及其别名的映射
        self.used_aliases = set()  # 存储已使用的别名
    
    def process_test_files(self) -> List[str]:
        """
        处理测试文件夹中的所有 Python 文件，提取并去重 import 语句
        
        Returns:
            去重后的 import 语句列表
        """
        for root, _, files in os.walk(self.test_folder_path):
            for file in files:
                if file.endswith('.py'):
                    file_path = os.path.join(root, file)
                    self._extract_imports_from_file(file_path)
        
        return self._generate_unique_imports()
    
    def _extract_imports_from_file(self, file_path: str) -> None:
        """
        从单个文件中提取 import 语句
        
        Args:
            file_path: 文件路径
        """
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                file_content = f.read()
            
            # 使用 AST 解析 Python 文件
            tree = ast.parse(file_content)
            
            for node in ast.walk(tree):
                # 处理 import xxx 形式
                if isinstance(node, ast.Import):
                    for name in node.names:
                        module_name = name.name
                        alias = name.asname or module_name.split('.')[-1]
                        
                        self.module_aliases[module_name].add(alias)
                        self.used_aliases.add(alias)
                
                # 处理 from xxx import yyy 形式
                elif isinstance(node, ast.ImportFrom):
                    if node.module is not None:  # 排除 from . import xxx 的情况
                        module_name = node.module
                        for name in node.names:
                            imported_name = name.name
                            alias = name.asname or imported_name
                            
                            import_str = f"from {module_name} import {imported_name}"
                            if name.asname:
                                import_str += f" as {alias}"
                            
                            self.import_statements.add(import_str)
                            self.used_aliases.add(alias)
        
        except Exception as e:
            print(f"Error processing file {file_path}: {e}")
    
    def _generate_unique_imports(self) -> List[str]:
        """
        生成去重后的 import 语句
        
        Returns:
            去重后的 import 语句列表
        """
        result = list(self.import_statements)
        
        # 跟踪已使用的别名，避免重复
        used_aliases = set()
        alias_counter = defaultdict(int)
        
        # 处理 import xxx as yyy 形式的语句
        for module, aliases in sorted(self.module_aliases.items()):  # 排序以确保结果一致性
            # 如果有多个别名，选择一个（优先选择与模块名最后一部分相同的别名）
            preferred_alias = module.split('.')[-1]
            
            # 如果首选别名在别名集合中且未被使用，使用它
            if preferred_alias in aliases and preferred_alias not in used_aliases:
                chosen_alias = preferred_alias
            else:
                # 如果首选别名已被使用或不在别名集合中
                # 生成一个唯一的别名
                base_alias = module.split('.')[-1]
                chosen_alias = base_alias
                
                # 如果别名已被使用，添加数字后缀
                if chosen_alias in used_aliases:
                    alias_counter[base_alias] += 1
                    chosen_alias = f"{base_alias}_{alias_counter[base_alias]}"
            
            used_aliases.add(chosen_alias)
            
            # 构建 import 语句
            if chosen_alias == module.split('.')[-1]:
                result.append(f"import {module}")
            else:
                result.append(f"import {module} as {chosen_alias}")
        
        # 排序以保持一致性
        return sorted(result)

    
    def save_imports_to_file(self, output_file: str) -> None:
        """
        将去重后的 import 语句保存到文件
        
        Args:
            output_file: 输出文件路径
        """
        imports = self.process_test_files()
        with open(output_file, 'w', encoding='utf-8') as f:
            for import_stmt in imports:
                f.write(f"{import_stmt}\n")


if __name__ == "__main__":
    # 创建 ImportGenerator 实例
    generator = ImportGenerator("/path/to/project/tests")
    
    # 处理测试文件并获取去重后的 import 语句
    unique_imports = generator.process_test_files()
    
    # 打印去重后的 import 语句
    for import_stmt in unique_imports:
        print(import_stmt)
    
    # 或者保存到文件
    # generator.save_imports_to_file("unique_imports.py")
