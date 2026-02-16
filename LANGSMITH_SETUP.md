# LangSmith Tracing Setup

LangSmith provides observability and monitoring for your LLM applications.

## Setup Steps

### 1. Create LangSmith Account
- Go to https://smith.langchain.com/
- Sign up for a free account

### 2. Get API Key
- Navigate to Settings → API Keys
- Create a new API key
- Copy the key

### 3. Update .env File
Replace `your_langsmith_api_key_here` in `.env` with your actual API key:

```env
LANGCHAIN_TRACING_V2=true
LANGCHAIN_ENDPOINT=https://api.smith.langchain.com
LANGCHAIN_API_KEY=ls-your-actual-key-here
LANGCHAIN_PROJECT=ai-learning-agent
```

### 4. Install Dependencies
```bash
pip install -r requirements.txt
```

### 5. Restart Backend
```bash
cd backend
python main.py
```

## What You'll See in LangSmith

Once configured, you'll be able to monitor:
- ✅ All LLM calls (spelling correction, content generation, quiz creation)
- ✅ Execution time for each function
- ✅ Token usage and costs
- ✅ Input/output for each step
- ✅ Error traces and debugging info
- ✅ Performance metrics

## Traced Functions

All these functions are now traced:
1. `gather_context` - Topic content generation
2. `validate_context` - Content relevance scoring
3. `explain_concept` - Detailed explanations
4. `generate_quiz` - Quiz question generation
5. `evaluate_student` - Answer evaluation
6. `feynman_explain` - Simplified explanations

## Disable Tracing (Optional)

To disable tracing, set in `.env`:
```env
LANGCHAIN_TRACING_V2=false
```

## View Traces

Visit: https://smith.langchain.com/
- Select your project: "ai-learning-agent"
- View all traces in real-time
