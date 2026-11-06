# My Projects and Research

This document describes some of the academic, research and software projects I have worked on or developed as proposals. It includes their objectives, technologies, technical approaches and the problems they aim to solve.

# 1. SentinelEdge

## Project Overview

SentinelEdge is a conceptual research proposal focused on developing a Byzantine-resilient Federated Learning framework for intrusion detection in MQTT-based Internet of Things (IoT) and Industrial Control Systems (ICS).

The primary motivation behind this research is to improve intrusion detection while preserving the privacy of distributed IoT devices. Instead of requiring all devices to share their raw data with a central server, Federated Learning allows participants to train models collaboratively.

## Problem Statement

Traditional centralized intrusion detection systems may require collecting data from multiple devices at a central location. This creates privacy concerns and can introduce security vulnerabilities.

Federated Learning helps address the data-sharing problem, but malicious or compromised participants can send manipulated model updates that affect the global model.

SentinelEdge proposes a Byzantine-resilient approach to address this challenge.

## Targeted Attacks

The research focuses on four attack categories:

- Reconnaissance
- Man-in-the-Middle (MitM)
- Replay attacks
- Zero-day attacks

## Proposed Technical Architecture

The proposed framework explores multiple detection and defense components:

- Temporal Convolutional Networks (TCN) for reconnaissance detection.
- CNN-BiLSTM for MitM attack detection.
- Transformer-based detection for replay attacks.
- Federated learning using the Flower framework.
- FedProx for federated model optimization.
- Additional defenses against malicious model updates.

The research also explores privacy-preserving mechanisms such as Differential Privacy and Secure Aggregation.

## Research Status

SentinelEdge is a conceptual research proposal presented at ICARMP 2026 at UMT Lahore. The work was presented in the conference poster category.

The proposed architecture and methodology were developed as research concepts. The framework had not yet undergone full implementation or experimental evaluation at the time of presentation.

## What I Learned

This research helped me explore Federated Learning, IoT security, intrusion detection, Byzantine attacks, deep learning architectures and privacy-preserving machine learning.

# 2. VaultIQ

## Project Overview

VaultIQ is a proposed secure academic document management platform designed to help students organize and share important academic and personal documents.

The idea is inspired by zero-trust security principles and aims to provide students with a secure digital vault.

## Problem Statement

Students often store important documents across different devices, email accounts and cloud storage platforms. Sharing sensitive documents with universities, recruiters and other organizations can create privacy and security risks.

VaultIQ aims to provide a centralized and secure way to manage these documents.

## Proposed Features

- Secure document storage.
- End-to-end encryption.
- Multi-factor authentication.
- Zero-trust access control.
- Expiring document-sharing links.
- Controlled access for recruiters and universities.
- AI-assisted document organization and detection.

## Technical Direction

The proposed architecture takes inspiration from security concepts such as Zero Trust, Zero Knowledge and least-privilege access.

The goal is to give users greater control over their documents and decide who can access them and for how long.

## Project Status

VaultIQ is an innovation and entrepreneurship project concept. Its proposed features and architecture should not be confused with a fully implemented production security platform.

## What I Learned

Developing the VaultIQ concept helped me explore application security, encryption, authentication, access control, privacy and security-oriented system architecture.

# 3. MindBridge RAG — Career Anxiety Assistant

## Project Overview

MindBridge is an academic project focused on building a Retrieval-Augmented Generation (RAG) application related to career anxiety.

The goal is to help users obtain relevant, context-based responses using a curated knowledge base.

## Problem Statement

Students experiencing career uncertainty may struggle to find relevant and reliable information about their concerns.

A conversational assistant can help retrieve relevant information from a knowledge base and present it in a more accessible format.

## Technical Approach

The project explores:

- Retrieval-Augmented Generation.
- Document processing and text chunking.
- Knowledge-base retrieval.
- Context-based answer generation.
- Evaluation using benchmark questions.
- Comparison of generated answers against ideal answers.

The project includes structured evaluation resources such as benchmark questions, ideal answers and risk labels.

## Technologies and Tools

The project uses Python and Gradio for its application interface, alongside RAG-related tools and language-model integrations.

## Project Status

MindBridge was developed as an academic group project. Its implementation and evaluation work focused on career-anxiety-related questions and comparing generated responses with expected answers.

## What I Learned

This project helped me understand how retrieval-based AI systems work, why context matters in LLM applications, and how generated answers can be evaluated using benchmark datasets.

# 4. My Research and Technical Interests

My interests include:

- Artificial Intelligence and Machine Learning.
- Deep Learning.
- Cybersecurity and penetration testing.
- IoT security.
- Federated Learning.
- Retrieval-Augmented Generation.
- Privacy-preserving technologies.
- Secure software development.

I particularly enjoy exploring projects that combine AI and cybersecurity to solve practical problems.

# 5. My Future Project Goals

I want to develop technically strong projects that combine artificial intelligence, cybersecurity and practical software engineering.

I also want to improve my ability to design secure systems, conduct technical research, implement machine learning models and build projects that demonstrate practical engineering skills.