# AttentionX-AI-Hackathon
AI Content Intelligence Platform
VIRAL INTELLIGENCE

Real AI scoring · Face emotion tracking · Viral clip detection · Computer vision CTR analysis

Live Demo: https://attention-x-ai-hackathon.vercel.app/
GitHub: github.com/abhishekakhand737/AttentionX-AI-Hackathon

Video : "C:\Users\abhishek\Downloads\ViralIQ_v3___AI_Content_Intelligence_and_1_more_page_-_Personal_-_Microsoft__Edge_2026-04-18_17-05-14.mp4"

📌 What is ViralIQ?
ViralIQ v3 is an AI-powered content intelligence platform that helps creators, marketers, and growth hackers analyze and optimize their short-form video content for maximum virality. It combines Claude AI (NLP), computer vision, and viral signal detection into one seamless tool.
Whether you have a YouTube URL, an Instagram Reel, a content topic, or a thumbnail image — ViralIQ tells you exactly how likely it is to go viral and why.

🚀 Features
⚡ URL / Topic Analyzer

Paste any YouTube, YouTube Shorts, or Instagram Reels URL — or just type a topic
Claude NLP analyzes the content and returns:

Viral IQ Score with reasoning
Hook power matrix
Sentiment analysis & content DNA extraction
Viral velocity vectors
Actionable AI recommendations


Supports auto-detection or manual platform selection (YouTube, Reels, Shorts, Topic)

👁️ Face Emotion / Thumbnail CTR Analyzer

Upload a thumbnail image (JPG, PNG, WEBP)
Runs entirely in-browser — no server upload, full privacy
Computer vision detects facial emotions in thumbnails
Predicts Click-Through Rate (CTR) impact based on emotion signals

Shocked / surprised faces → proven higher CTR


No image? Use the AI Emotion Scorer — describe your thumbnail in text and get a CTR prediction powered by Claude

✂️ Viral Clip Detector (Long → Short)

Paste a YouTube URL or a video transcript/description
AI detects the top 3 viral moments with timestamps
Explains why each clip will perform well on short-form platforms
Perfect for repurposing long-form content into Shorts/Reels


🧠 Tech Stack
LayerTechnologyAI / NLP EngineClaude AI (Anthropic)Computer VisionIn-browser face detectionFrontendHTML, CSS, JavaScriptHostingVercelArchitectureClient-side first, no data stored

🏗️ How It Works
User Input (URL / Topic / Image / Transcript)
        ↓
Platform Detection (YouTube / Reels / Shorts / Topic)
        ↓
Claude NLP Pipeline:
  → Content DNA Extraction
  → Sentiment Analysis
  → Hook Power Scoring
  → Viral Velocity Calculation
  → AI Recommendations
        ↓
Output: Viral IQ Score + Actionable Insights
For thumbnails, the flow is:
Image Upload (client-side)
        ↓
Face Detection & Emotion Classification
        ↓
CTR Prediction Score + Emotion Breakdown

🎯 Use Cases

Content Creators — Validate ideas before spending time producing
Social Media Managers — Optimize existing content for resharing
Growth Hackers — Identify high-performing content patterns
Video Editors — Find the best clips from long-form videos to repurpose


🛠️ Local Development
bash# Clone the repository
git clone https://github.com/abhishekakhand737/AttentionX-AI-Hackathon
cd AttentionX-AI-Hackathon

# Install dependencies (if applicable)
npm install

# Run locally
npm run dev
# or simply open index.html in your browser

The app is mostly client-side. For AI features, ensure your Claude API key is configured in environment variables.

envANTHROPIC_API_KEY=your_key_here

🌐 Deployment
The project is deployed on Vercel with zero-config deployment:
bashvercel deploy

🔮 Roadmap / Future Features

 Direct Youtube URL support
 Batch URL analysis
 Historical viral trend comparison
 Chrome Extension for one-click analysis while browsing
 Export reports as PDF
 Dashboard for tracking content performance over time


🙌 Built For
Attention X AI Hackathon — Built to explore the intersection of generative AI, computer vision, and social media growth mechanics.

📄 License
MIT License © 2025 ViralIQ

💬 Contact
GitHub: github.com/abhishekakhand737/AttentionX-AI-Hackathon
