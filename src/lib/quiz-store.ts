import { create } from "zustand";
import { persist } from "zustand/middleware";
import type { Letter } from "@/data/types";

export type Mode = "practice" | "exam";

type State = {
  practice: Record<number, Letter>;
  exam: Record<number, Letter>;
  flagged: number[];
  practiceIndex: number;
  examIndex: number;
  examStarted: boolean;
  examSubmitted: boolean;
  examStartedAt: number | null;
  examFinishedAt: number | null;
  setPractice: (id: number, letter: Letter) => void;
  setExam: (id: number, letter: Letter) => void;
  toggleFlag: (id: number) => void;
  setPracticeIndex: (n: number) => void;
  setExamIndex: (n: number) => void;
  startExam: () => void;
  submitExam: () => void;
  resetPractice: () => void;
  resetExam: () => void;
};

export const useQuizStore = create<State>()(
  persist(
    (set, get) => ({
      practice: {},
      exam: {},
      flagged: [],
      practiceIndex: 1,
      examIndex: 1,
      examStarted: false,
      examSubmitted: false,
      examStartedAt: null,
      examFinishedAt: null,
      setPractice: (id, letter) =>
        set({ practice: { ...get().practice, [id]: letter } }),
      setExam: (id, letter) => {
        if (get().examSubmitted) return;
        set({ exam: { ...get().exam, [id]: letter } });
      },
      toggleFlag: (id) => {
        const flagged = get().flagged;
        set({
          flagged: flagged.includes(id)
            ? flagged.filter((x) => x !== id)
            : [...flagged, id],
        });
      },
      setPracticeIndex: (n) => set({ practiceIndex: n }),
      setExamIndex: (n) => set({ examIndex: n }),
      startExam: () =>
        set({
          examStarted: true,
          examSubmitted: false,
          exam: {},
          examIndex: 1,
          examStartedAt: Date.now(),
          examFinishedAt: null,
        }),
      submitExam: () =>
        set({
          examSubmitted: true,
          examStarted: true,
          examFinishedAt: Date.now(),
        }),
      resetPractice: () => set({ practice: {}, practiceIndex: 1 }),
      resetExam: () =>
        set({
          exam: {},
          examIndex: 1,
          examStarted: false,
          examSubmitted: false,
          examStartedAt: null,
          examFinishedAt: null,
        }),
    }),
    { name: "epi-aula6-quiz" },
  ),
);
