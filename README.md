# LLM Orchestrator                                                                                                                                                 
                                                            
  > A unified FastAPI service for multi-provider LLM calls — with caching, observability, and cost tracking baked in.                                                
   
  **Status:** 🚧 in active development — built as a portfolio project alongside my Winter 2027 internship prep.                                                      
                                                            
  ## What it does                                                                                                                                                    
                                                            
  LLM Orchestrator sits in front of OpenAI, Anthropic, and local Ollama models, giving your app a single API endpoint to call. It handles:                           
   
  - 🧠 **Multi-provider routing** — call any LLM through a single interface                                                                                          
  - 💾 **Semantic caching** — embeds the request, checks for similar prior queries, serves cached responses when the cosine similarity is high enough
  - 📊 **Observability dashboard** — a Next.js UI showing latency, token cost, and cache hit rate per model in real time                                             
  - 🛡️  **Guardrails** — rate limiting per API key, PII filtering before requests hit the model, structured retry logic on 5xx                                        
  - 📝 **Request logging** — every prompt/response stored in Postgres for later analysis                                                                             
                                                                                                                                                                     
  ## Why I built this                                                                                                                                                
                                                                                                                                                                     
  I co-founded **Nexus**, an AI customer-comms tool now used daily by a paying business. While building Nexus, I hit the same problems over and over: token costs    
  blowing up, no easy way to compare model performance, and no observability into what was actually happening when the GPT call took 8 seconds. This is the
  open-sourced solution to those problems.                                                                                                                           
                                                            
  ## Stack

  | Layer | Tech |
  |---|---|
  | API | Python · FastAPI |
  | Cache | Redis (semantic similarity via embedding index) |                                                                                                        
  | Database | PostgreSQL |
  | Frontend | Next.js · React · Tailwind |                                                                                                                          
  | LLM providers | OpenAI · Anthropic · Ollama (local) |                                                                                                            
  | Deployment | Docker · GitHub Actions CI/CD |
                                                                                                                                                                     
  ## Architecture (planned)                                 
                                                                                                                                                                     
  Client → FastAPI gateway → [cache check] → LLM provider   
                                ↓                ↓
                            Redis cache    Postgres log                                                                                                              
                                ↓                ↓
                            Next.js dashboard (live metrics)                                                                                                         
                                                                                                                                                                     
  ## Roadmap
                                                                                                                                                                     
  - [ ] FastAPI scaffold with OpenAI provider               
  - [ ] Anthropic + Ollama providers
  - [ ] Redis-backed semantic cache (embeddings comparison)                                                                                                          
  - [ ] Postgres request logging schema
  - [ ] Rate limiting + PII filtering middleware                                                                                                                     
  - [ ] Next.js dashboard (latency, cost, hit rate)         
  - [ ] Docker compose + deploy                                                                                                                                      
  - [ ] Open-source release with `pip install` package                                                                                                               
  
  ## Author                                                                                                                                                          
                                                            
  Built by [Vansh Taneja](https://github.com/vanshtaneja23) — 4th-year Computing Science student at the University of Alberta, currently a Software Developer Co-op  
  at the City of Edmonton and co-founder of Nexus.
                                                                                                                                                                     
  ## License                                                

  MIT
