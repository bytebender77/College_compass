import React, { useState, useRef, useEffect } from 'react';
import { Send, BookOpen, Sparkles, Loader2, Copy, Check, Compass } from 'lucide-react';

export default function CampusCompass() {
  const [question, setQuestion] = useState('');
  const [messages, setMessages] = useState([]);
  const [isLoading, setIsLoading] = useState(false);
  const [copiedIndex, setCopiedIndex] = useState(null);
  const messagesEndRef = useRef(null);

  // Get API URL from environment variable or use default
  // Try to detect if we're in development (Vite) or production
  const getApiUrl = () => {
    // Check for environment variable first (for production builds)
    if (import.meta.env.VITE_API_URL) {
      return import.meta.env.VITE_API_URL;
    }
    
    // In production (not dev mode), use same origin or detect from window location
    if (!import.meta.env.DEV) {
      // If deployed on same domain as backend, use relative URL
      // Otherwise, try to detect backend URL from window location
      const hostname = window.location.hostname;
      // If on render.com, backend might be on different subdomain
      if (hostname.includes('render.com') || hostname.includes('onrender.com')) {
        // For Render, backend is typically on a different service
        // You'll need to set VITE_API_URL in production
        return window.location.origin.replace(/^https?:\/\/([^.]+)/, 'https://$1-api') || 'http://localhost:8000';
      }
      // For same domain deployment, use relative URL
      return window.location.origin;
    }
    
    // In development, try to use the current host with port 8000
    return `http://${window.location.hostname}:8000`;
  };
  
  const API_URL = getApiUrl();

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  };

  useEffect(() => {
    scrollToBottom();
  }, [messages]);

  const exampleQuestions = [
    "What are the hostel rules?",
    "What is the fee structure for M.Tech programs?",
    "When does the academic calendar start?",
    "What are the library regulations?"
  ];

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!question.trim()) return;

    const userMessage = { type: 'user', content: question };
    setMessages(prev => [...prev, userMessage]);
    const currentQuestion = question;
    setQuestion('');
    setIsLoading(true);

    try {
      // API call to backend
      const response = await fetch(`${API_URL}/api/answer`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ question: currentQuestion })
      });

      if (!response.ok) {
        throw new Error(`API error: ${response.status} ${response.statusText}`);
      }

      const data = await response.json();
      
      const aiMessage = {
        type: 'ai',
        content: data.answer,
        sources: data.sources // Format: [{ name: "file.pdf", page: 2 }]
      };
      setMessages(prev => [...prev, aiMessage]);
    } catch (error) {
      console.error('Error fetching answer:', error);
      let errorMessage = {
        type: 'ai',
        content: '',
        sources: []
      };
      
      // Provide more specific error messages
      if (error.message.includes('Failed to fetch') || error.message.includes('NetworkError')) {
        errorMessage.content = `❌ Cannot connect to the backend server at ${API_URL}. Please make sure the backend is running. Start it with: python app.py`;
      } else if (error.message.includes('404')) {
        errorMessage.content = `❌ API endpoint not found. Please check that the backend is running and the API URL is correct: ${API_URL}`;
      } else if (error.message.includes('500')) {
        errorMessage.content = `❌ Server error. The backend encountered an issue processing your question. Please try again or rephrase your question.`;
      } else {
        errorMessage.content = `❌ Error: ${error.message}. Please make sure the backend server is running at ${API_URL} and try again.`;
      }
      
      setMessages(prev => [...prev, errorMessage]);
    } finally {
      setIsLoading(false);
    }
  };

  const handleExampleClick = (example) => {
    setQuestion(example);
  };

  const copyToClipboard = (text, index) => {
    navigator.clipboard.writeText(text);
    setCopiedIndex(index);
    setTimeout(() => setCopiedIndex(null), 2000);
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-gray-950 via-slate-900 to-gray-950 text-gray-100">
      {/* Animated Background */}
      <div className="fixed inset-0 overflow-hidden pointer-events-none">
        <div className="absolute top-1/4 -left-48 w-96 h-96 bg-cyan-500/10 rounded-full blur-3xl animate-pulse"></div>
        <div className="absolute bottom-1/4 -right-48 w-96 h-96 bg-purple-500/10 rounded-full blur-3xl animate-pulse" style={{ animationDelay: '1s' }}></div>
        <div className="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-96 h-96 bg-blue-500/5 rounded-full blur-3xl animate-pulse" style={{ animationDelay: '2s' }}></div>
      </div>

      {/* Header */}
      <header className="relative border-b border-cyan-500/20 bg-gray-900/50 backdrop-blur-xl">
        <div className="max-w-6xl mx-auto px-6 py-4">
          <div className="flex items-center gap-3">
            <div className="relative">
              <Compass className="w-10 h-10 text-cyan-400" />
              <div className="absolute inset-0 blur-xl bg-cyan-400/30"></div>
            </div>
            <div>
              <h1 className="text-3xl font-bold bg-gradient-to-r from-cyan-400 via-blue-400 to-purple-400 bg-clip-text text-transparent">
                Campus Compass
              </h1>
              <p className="text-sm text-gray-400">Your Intelligent Campus Guide</p>
            </div>
          </div>
        </div>
      </header>

      {/* Main Content */}
      <main className="relative max-w-6xl mx-auto px-6 py-8">
        {/* Welcome Section */}
        {messages.length === 0 && (
          <div className="mb-12 text-center space-y-6 animate-fade-in">
            <div className="relative inline-block">
              <Sparkles className="w-16 h-16 text-cyan-400 mx-auto" />
              <div className="absolute inset-0 blur-2xl bg-cyan-400/30"></div>
            </div>
            <div>
              <h2 className="text-4xl font-bold mb-3 bg-gradient-to-r from-cyan-300 via-blue-300 to-purple-300 bg-clip-text text-transparent">
                Ask Me Anything About Campus
              </h2>
              <p className="text-gray-400 text-lg">
                Get instant answers from official campus documents
              </p>
            </div>

            {/* Example Questions */}
            <div className="grid md:grid-cols-2 gap-3 max-w-3xl mx-auto mt-8">
              {exampleQuestions.map((example, idx) => (
                <button
                  key={idx}
                  onClick={() => handleExampleClick(example)}
                  className="group relative overflow-hidden p-4 rounded-xl bg-gradient-to-br from-gray-800/50 to-gray-900/50 border border-cyan-500/20 hover:border-cyan-400/50 transition-all duration-300 text-left"
                >
                  <div className="absolute inset-0 bg-gradient-to-r from-cyan-500/0 via-cyan-500/5 to-cyan-500/0 opacity-0 group-hover:opacity-100 transition-opacity"></div>
                  <BookOpen className="w-5 h-5 text-cyan-400 mb-2" />
                  <p className="text-sm text-gray-300 group-hover:text-gray-100 transition-colors">
                    {example}
                  </p>
                </button>
              ))}
            </div>
          </div>
        )}

        {/* Messages */}
        <div className="space-y-6 mb-6">
          {messages.map((msg, idx) => (
            <div
              key={idx}
              className={`flex ${msg.type === 'user' ? 'justify-end' : 'justify-start'} animate-slide-up`}
            >
              <div className={`max-w-3xl ${msg.type === 'user' ? 'w-auto' : 'w-full'}`}>
                {msg.type === 'user' ? (
                  <div className="relative group">
                    <div className="absolute inset-0 bg-gradient-to-r from-cyan-500 to-blue-500 rounded-2xl blur-lg opacity-50 group-hover:opacity-75 transition-opacity"></div>
                    <div className="relative bg-gradient-to-r from-cyan-500 to-blue-500 text-white px-6 py-4 rounded-2xl shadow-xl">
                      {msg.content}
                    </div>
                  </div>
                ) : (
                  <div className="relative group">
                    <div className="absolute -inset-1 bg-gradient-to-r from-cyan-500/20 via-purple-500/20 to-blue-500/20 rounded-2xl blur-lg opacity-50 group-hover:opacity-75 transition-opacity"></div>
                    <div className="relative bg-gray-800/50 backdrop-blur-xl border border-cyan-500/20 px-6 py-4 rounded-2xl shadow-xl">
                      <div className="flex items-start justify-between gap-3 mb-3">
                        <div className="flex items-center gap-2">
                          <Compass className="w-5 h-5 text-cyan-400" />
                          <span className="font-semibold text-cyan-400">Campus Compass</span>
                        </div>
                        <button
                          onClick={() => copyToClipboard(msg.content, idx)}
                          className="p-1.5 hover:bg-gray-700/50 rounded-lg transition-colors"
                        >
                          {copiedIndex === idx ? (
                            <Check className="w-4 h-4 text-green-400" />
                          ) : (
                            <Copy className="w-4 h-4 text-gray-400" />
                          )}
                        </button>
                      </div>
                      <p className="text-gray-200 leading-relaxed whitespace-pre-wrap">
                        {msg.content}
                      </p>
                    </div>
                  </div>
                )}
              </div>
            </div>
          ))}
          {isLoading && (
            <div className="flex justify-start animate-slide-up">
              <div className="relative max-w-3xl">
                <div className="absolute -inset-1 bg-gradient-to-r from-cyan-500/20 via-purple-500/20 to-blue-500/20 rounded-2xl blur-lg opacity-50"></div>
                <div className="relative bg-gray-800/50 backdrop-blur-xl border border-cyan-500/20 px-6 py-4 rounded-2xl shadow-xl">
                  <div className="flex items-center gap-3">
                    <Loader2 className="w-5 h-5 text-cyan-400 animate-spin" />
                    <span className="text-gray-400">Searching campus documents...</span>
                  </div>
                </div>
              </div>
            </div>
          )}
          <div ref={messagesEndRef} />
        </div>

        {/* Input Form */}
        <div className="sticky bottom-6">
          <form onSubmit={handleSubmit} className="relative max-w-4xl mx-auto">
            <div className="absolute -inset-1 bg-gradient-to-r from-cyan-500 via-blue-500 to-purple-500 rounded-2xl blur-lg opacity-50"></div>
            <div className="relative flex items-center gap-3 bg-gray-900/90 backdrop-blur-xl border border-cyan-500/30 rounded-2xl p-3 shadow-2xl">
              <input
                type="text"
                value={question}
                onChange={(e) => setQuestion(e.target.value)}
                placeholder="Ask about hostel rules, fees, calendar, library..."
                className="flex-1 bg-transparent text-gray-100 placeholder-gray-500 outline-none px-3 py-2 text-lg"
                disabled={isLoading}
              />
              <button
                type="submit"
                disabled={isLoading || !question.trim()}
                className="relative group px-6 py-3 bg-gradient-to-r from-cyan-500 to-blue-500 rounded-xl font-semibold transition-all duration-300 hover:shadow-lg hover:shadow-cyan-500/50 disabled:opacity-50 disabled:cursor-not-allowed"
              >
                <div className="absolute inset-0 bg-gradient-to-r from-cyan-400 to-blue-400 rounded-xl opacity-0 group-hover:opacity-100 transition-opacity blur"></div>
                <div className="relative flex items-center gap-2">
                  {isLoading ? (
                    <Loader2 className="w-5 h-5 animate-spin" />
                  ) : (
                    <Send className="w-5 h-5" />
                  )}
                  <span>Ask</span>
                </div>
              </button>
            </div>
          </form>
        </div>
      </main>

      <style>{`
        @keyframes slide-up {
          from {
            opacity: 0;
            transform: translateY(20px);
          }
          to {
            opacity: 1;
            transform: translateY(0);
          }
        }
        
        @keyframes fade-in {
          from {
            opacity: 0;
          }
          to {
            opacity: 1;
          }
        }
        
        .animate-slide-up {
          animation: slide-up 0.4s ease-out;
        }
        
        .animate-fade-in {
          animation: fade-in 0.6s ease-out;
        }
      `}</style>
    </div>
  );
}

