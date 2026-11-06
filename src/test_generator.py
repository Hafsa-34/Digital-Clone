
from generator import DigitalCloneGenerator

generator = DigitalCloneGenerator()

# Test using a question supported by your notes
sample_chunks = [
    {
        "source": "07-Goals&FuturePlans.md",
        "section": "Career Goals",
        "text": (
            "My current job is in Software QA. "
            "My long-term career goal is to become "
            "a professional penetration tester."
        )
    }
]

question = "What is my long-term career goal?"

answer = generator.generate(question, sample_chunks)

print("\nQuestion:", question)
print("\nGenerated Answer:", answer)

# Test the honest fallback
unknown_question = "What is my favourite car?"

unknown_answer = generator.generate(
    unknown_question,
    sample_chunks
)

print("\nUnknown Question:", unknown_question)
print("\nFallback Test:", unknown_answer)
