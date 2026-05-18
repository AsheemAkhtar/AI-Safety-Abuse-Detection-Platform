# AI-Safety-Abuse-Detection-Platform LIVE DEMO: https://d3pl0aasprp2v.cloudfront.net

A multi-domain Trust & Safety system designed to detect harmful content across comments, SMS, and emails using NLP embeddings, statistical risk scoring, and LLM-powered moderation analysis.

Features
Harmful content detection for:
Toxic comments
Spam SMS
Fraudulent emails
Transformer embedding-based classification
Configurable risk threshold slider
Real-time risk visualization dashboard
LLM-generated moderation insights using Groq API
Serverless deployment using AWS Lambda + Docker
Frontend hosted on AWS S3 + CloudFront
Tech Stack
Python
FastAPI
Sentence Transformers
Scikit-learn
Chart.js
Groq API
Docker
AWS Lambda
AWS ECR
AWS S3
AWS CloudFront
Model Pipeline
Text input is embedded using transformer embeddings
Logistic Regression classifier predicts risk probability
Risk score is evaluated against configurable threshold
LLM generates moderation reasoning and recommendations
Frontend visualizes safety metrics in real time
Deployment Architecture
CloudFront
    ↓
S3 Static Frontend
    ↓
Lambda Function URL
    ↓
Dockerized FastAPI Backend
Example Use Cases
AI safety monitoring
Fraud and abuse detection
Content moderation systems
Trust & Safety analytics
Human review prioritization
