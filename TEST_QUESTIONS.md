# Test Questions for Campus Compass

A comprehensive list of questions to test the Campus Compass RAG system across different document types and topics.

## 📚 Academic Calendar & Examinations

1. **What is the minimum attendance required to appear for end-semester exams?**
2. **When does the academic calendar start for B.Tech students?**
3. **What are the important dates for the odd semester?**
4. **When is the last date for course withdrawal?**
5. **What is the schedule for mid-semester examinations?**
6. **When does the even semester begin?**
7. **What are the registration dates for the new academic year?**
8. **When are the end-semester examinations conducted?**
9. **What is the academic calendar for M.Tech students?**
10. **When is the last date for fee submission?**

## 🏠 Hostel Rules & Regulations

11. **What are the hostel rules and regulations?**
12. **What are the curfew timings in the hostel?**
13. **Are visitors allowed in the hostel rooms?**
14. **What are the rules regarding hostel fees?**
15. **What is the procedure for hostel room allocation?**
16. **What are the rules for hostel maintenance?**
17. **Can students stay in the hostel during holidays?**
18. **What are the penalties for violating hostel rules?**
19. **What are the rules for hostel mess facilities?**
20. **What is the procedure for hostel check-in and check-out?**

## 📖 Library Rules & Regulations

21. **What are the library rules and regulations?**
22. **What is the fine for late return of library books?**
23. **How many books can a student borrow from the library?**
24. **What are the library timings?**
25. **What is the procedure for library membership?**
26. **What are the rules for using library computers?**
27. **What is the penalty for losing a library book?**
28. **Can students access library resources online?**
29. **What are the rules for library study rooms?**
30. **What is the renewal policy for library books?**

## 💰 Fee Structure

31. **What is the fee structure for B.Tech programs?**
32. **What is the fee structure for M.Tech programs?**
33. **What is the fee structure for MBA programs?**
34. **What is the fee structure for Ph.D. programs?**
35. **What are the components of the fee structure?**
36. **What is the medical fee?**
37. **What are the hostel fees?**
38. **What is the late fee for delayed payment?**
39. **Are there any scholarships or fee waivers available?**
40. **What is the fee payment schedule?**

## 📋 Admission & Brochure

41. **What are the admission requirements for B.Tech?**
42. **What is the admission process for M.Tech?**
43. **What are the eligibility criteria for Ph.D. admission?**
44. **What documents are required for admission?**
45. **What is the admission deadline?**
46. **What are the selection criteria for admission?**
47. **What is the admission fee?**
48. **What programs are offered at the institute?**
49. **What are the specializations available?**
50. **What is the admission process for international students?**

## 📜 Rules & Regulations

51. **What is the code of conduct for students?**
52. **What are the disciplinary policies?**
53. **What are the rules regarding student misconduct?**
54. **What are the safety regulations on campus?**
55. **What are the rules for using institute facilities?**
56. **What is the policy on academic integrity?**
57. **What are the rules for using computing services?**
58. **What are the regulations for student organizations?**
59. **What is the grievance redressal procedure?**
60. **What are the rules for using institute vehicles?**

## 🎓 Academic Policies

61. **What is the grading system?**
62. **What is the credit system?**
63. **What is the policy on course registration?**
64. **What are the rules for course withdrawal?**
65. **What is the policy on academic probation?**
66. **What are the rules for thesis submission?**
67. **What is the policy on plagiarism?**
68. **What are the rules for project work?**
69. **What is the policy on internships?**
70. **What are the rules for thesis defense?**

## 🔍 Complex/Multi-Document Questions

71. **If the academic calendar mentions exam week and the hostel rules restrict late-night entry during that time, what options does a student have for overnight study?**
72. **What are the consequences if a student has less than 75% attendance and wants to appear for end-semester exams?**
73. **What is the total cost including tuition, hostel, and medical fees for a B.Tech student?**
74. **What are the library rules regarding book returns during exam periods?**
75. **What are the disciplinary actions for violating both hostel and academic rules?**
76. **What is the procedure for fee payment if a student misses the deadline mentioned in the academic calendar?**
77. **What are the rules for using library resources while staying in the hostel?**
78. **What is the policy on attendance for students who are also working on research projects?**
79. **What are the safety regulations that apply to both hostel and academic buildings?**
80. **What is the complete admission process from application to hostel allocation?**

## 🧪 Edge Cases & Error Testing

81. **What is the weather like today?** (Should return "I don't know" - not in documents)
82. **What is the capital of France?** (Should return "I don't know" - not in documents)
83. **Tell me a joke.** (Should return "I don't know" - not in documents)
84. **What are the rules for using the swimming pool?** (May not be in documents)
85. **What is the WiFi password?** (Should return "I don't know" - not in documents)
86. **What are the cafeteria menu options?** (May not be in documents)
87. **What is the procedure for applying to other universities?** (Should return "I don't know" - not in documents)
88. **What are the rules for parking vehicles?** (May not be in documents)
89. **What is the procedure for getting a student ID card?** (May not be in documents)
90. **What are the rules for using the gym?** (May not be in documents)

## 📊 Performance Testing Questions

91. **What are all the important dates in the academic calendar?**
92. **List all the fees mentioned in the fee structure documents.**
93. **What are all the rules related to student conduct?**
94. **Summarize all the library regulations.**
95. **What are all the hostel rules regarding visitors?**
96. **List all the admission requirements for different programs.**
97. **What are all the safety regulations on campus?**
98. **Summarize all the disciplinary policies.**
99. **What are all the rules for using institute facilities?**
100. **List all the important policies mentioned in the documents.**

## 🎯 Quick Test Set (Top 10)

For quick testing, try these essential questions:

1. **What is the minimum attendance required to appear for end-semester exams?**
2. **What are the hostel rules?**
3. **What is the fee structure for M.Tech programs?**
4. **What are the library regulations?**
5. **When does the academic calendar start?**
6. **What is the code of conduct for students?**
7. **What are the admission requirements for B.Tech?**
8. **What is the fine for late library books?**
9. **What are the safety regulations?**
10. **What is the policy on student misconduct?**

## 💡 Tips for Testing

### Test Different Question Types:
- **Specific questions**: "What is the minimum attendance?"
- **General questions**: "What are the hostel rules?"
- **Date-based questions**: "When does the semester start?"
- **Procedure questions**: "What is the admission process?"
- **Policy questions**: "What is the code of conduct?"

### Test Edge Cases:
- Questions not in documents (should return "I don't know")
- Very specific questions
- Questions requiring information from multiple documents
- Questions with typos or unclear phrasing

### Verify Responses:
- ✅ Answers should be based on the provided context
- ✅ Should cite sources (even if not displayed in UI)
- ✅ Should say "I don't know" for information not in documents
- ✅ Should handle multi-document questions correctly

## 📝 Notes

- These questions are designed to test various aspects of the RAG system
- Some questions may not have answers in the current document set
- The system should gracefully handle questions it cannot answer
- Complex questions test the system's ability to combine information from multiple sources

