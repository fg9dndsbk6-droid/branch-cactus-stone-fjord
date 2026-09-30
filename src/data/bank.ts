import data from "./questions.json";
import type { Letter, Question } from "./types";

export const QUESTIONS = data as Question[];

export const THEMES = [...new Set(QUESTIONS.map((q) => q.tema))];

export function getQuestion(id: number): Question | undefined {
  return QUESTIONS.find((q) => q.id === id);
}

export function scoreOf(answers: Record<number, Letter>): {
  correct: number;
  total: number;
  byTheme: { tema: string; correct: number; total: number }[];
} {
  let correct = 0;
  const themeMap = new Map<string, { correct: number; total: number }>();
  for (const q of QUESTIONS) {
    const slot = themeMap.get(q.tema) ?? { correct: 0, total: 0 };
    slot.total += 1;
    if (answers[q.id] === q.answer) {
      correct += 1;
      slot.correct += 1;
    }
    themeMap.set(q.tema, slot);
  }
  return {
    correct,
    total: QUESTIONS.length,
    byTheme: [...themeMap.entries()].map(([tema, v]) => ({ tema, ...v })),
  };
}
