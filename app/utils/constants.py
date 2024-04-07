from enum import Enum

SUPPORTED_FILE_TYPES = ["application/pdf", "text/plain"]

class OpenAIModels(Enum):
    GPT3 = "text-davinci-003"
    GPT3_5_TURBO = "gpt-3.5-turbo"
    GPT4_TURBO = "gpt-4-turbo-preview"
    GPT4 = "gpt-4"

RESUME_REVIEW_PROMPT = """

Objective: Conduct a thorough evaluation of the provided resume, assigning a score out of 100 based on the universal criteria outlined below. Your feedback should be detailed, constructive, and tailored to enhance the applicant's presentation of their skills, experiences, and overall candidacy for their target job role. The feedback must be actionable, directly addressing both strengths and areas for improvement.

Scoring Criteria:

1. Relevance of Skills and Experience (0-25 Points): Evaluate the relevance of the applicant's skills and experiences to their targeted job role. This includes technical skills, industry-specific knowledge, soft skills, and the ability to demonstrate adaptability and growth in their career path.

2. Clarity and Conciseness (0-25 Points): Assess how effectively the resume communicates the applicant's qualifications. Is the information well-organized, easy to follow, and free from unnecessary jargon or verbosity?

3. Achievements and Impact (0-25 Points): Focus on the presentation of the applicant's achievements. Are outcomes quantified where possible? Are individual contributions and the impact of their work clearly outlined?

4. Design and Formatting (0-25 Points): Judge the professional appearance and readability of the resume. Does the design and layout facilitate easy scanning? Is the formatting consistent and appropriate for the applicant's industry?

Feedback Guidelines:

- Positives: Start with the strengths of the resume, including any particularly well-presented sections, impressive achievements, or unique qualifications that stand out.

- Areas for Improvement: Provide concrete suggestions for enhancing the resume. This may involve refining descriptions, including additional relevant details, restructuring the layout for better logic and flow, or adjusting the design for professional polish.

- Overall Impression: Summarize your comprehensive assessment of the resume, offering encouragement and emphasizing that strategic improvements can significantly elevate the applicant's presentation and appeal to employers.

- Final Score: Tally up and present the user's final resume score

Note to LLM: Your insights are invaluable in assisting the applicant to refine their resume. Your feedback should empower them to present their qualifications in the most effective manner, tailored to their desired career trajectory. Keep in mind that constructive criticism combined with positive reinforcement can greatly motivate the applicant to make impactful revisions. Please support all judgements made with specific examples cited from the provided text. Please strictly adhere to the scoring criteria and feedback guidelines provided.
"""


