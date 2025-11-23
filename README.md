# Replication Package of TestTailor

This replication package contains all the artifacts required to reproduce the experiments conducted in the TestTailor paper.

## Contents
**test-apps/**

A collection of real-world open-source projects used in the TestTailor evaluation.
These projects serve as the targets for test generation, augmentation, and coverage measurement during experiments.

**existing-tests/**

A set of baseline test cases generated using Codamosa with the GPT-4o LLM.
This directory is organized by module, where each subfolder corresponds to a specific code module from the target projects.
For example:
    - ansible.cli.adhoc/
    - cookiecutter.find/
    - flutils.fs/
...

Each subfolder contains the raw tests directly produced by Codamosa before any processing, filtering, or enhancement by TestTailor. These tests are used as a baseline in our comparative evaluation.