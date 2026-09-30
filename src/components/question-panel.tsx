import type { ReactNode } from "react";
import { Bookmark, Check, ChevronLeft, ChevronRight, X } from "lucide-react";
import { QUESTIONS } from "@/data/bank";
import type { Letter } from "@/data/types";
import { LETTERS } from "@/data/types";
import { Badge } from "@/components/ui/badge";
import { Button } from "@/components/ui/button";
import { Progress } from "@/components/ui/progress";
import { cn } from "@/lib/utils";

type Props = {
  id: number;
  selected?: Letter;
  flagged: boolean;
  reveal: boolean;
  onSelect: (letter: Letter) => void;
  onFlag: () => void;
  onPrev: () => void;
  onNext: () => void;
  onJump?: (id: number) => void;
  answeredIds?: number[];
  footer?: ReactNode;
};

export function QuestionPanel({
  id,
  selected,
  flagged,
  reveal,
  onSelect,
  onFlag,
  onPrev,
  onNext,
  onJump,
  answeredIds,
  footer,
}: Props) {
  const q = QUESTIONS[id - 1];
  if (!q) return null;
  const progress = (id / QUESTIONS.length) * 100;

  return (
    <article className="flex flex-col gap-6">
      <div className="flex flex-col gap-3">
        <div className="flex items-center justify-between gap-3">
          <p className="text-sm tabular-nums text-muted-foreground">
            Questão {String(id).padStart(2, "0")} de {QUESTIONS.length}
          </p>
          <Badge>{q.tema}</Badge>
        </div>
        <Progress value={progress} />
      </div>

      <div className="rounded-xl border border-border bg-card p-5 shadow-[0_1px_0_rgba(21,34,56,0.04)] sm:p-8">
        <h1 className="font-display text-xl font-medium leading-snug text-ink sm:text-2xl">
          {q.stem}
        </h1>

        <fieldset className="mt-6 flex flex-col gap-3" aria-label="Alternativas">
          <legend className="sr-only">Escolha uma alternativa</legend>
          {LETTERS.map((letter) => {
            const isSel = selected === letter;
            const isRight = q.answer === letter;
            const showOk = reveal && isRight;
            const showBad = reveal && isSel && !isRight;
            return (
              <button
                key={letter}
                type="button"
                onClick={() => onSelect(letter)}
                className={cn(
                  "flex min-h-14 items-start gap-3 rounded-lg border px-4 py-3.5 text-left transition-colors duration-[var(--motion-quick)]",
                  "focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring",
                  showOk && "border-ok bg-ok-soft text-ink",
                  showBad && "border-bad bg-bad-soft text-ink",
                  !showOk &&
                    !showBad &&
                    isSel &&
                    "border-primary bg-cream-deep",
                  !showOk &&
                    !showBad &&
                    !isSel &&
                    "border-border bg-card hover:bg-cream-deep",
                )}
              >
                <span
                  className={cn(
                    "mt-0.5 inline-flex size-7 shrink-0 items-center justify-center rounded-sm border text-sm font-semibold",
                    showOk && "border-ok bg-ok text-primary-foreground",
                    showBad && "border-bad bg-bad text-primary-foreground",
                    !showOk &&
                      !showBad &&
                      "border-border bg-background text-steel",
                  )}
                >
                  {showOk ? <Check className="size-3.5" /> : showBad ? <X className="size-3.5" /> : letter}
                </span>
                <span className="text-[15px] leading-relaxed sm:text-base">
                  {q.options[letter]}
                </span>
              </button>
            );
          })}
        </fieldset>

        {reveal && selected ? (
          <div
            className={cn(
              "mt-6 rounded-lg border px-4 py-4",
              selected === q.answer
                ? "border-ok/30 bg-ok-soft"
                : "border-bad/30 bg-bad-soft",
            )}
          >
            <p className="text-sm font-semibold tracking-wide text-ink">
              Gabarito: {q.answer}
              {selected === q.answer ? " · correta" : " · sua marca estava em " + selected}
            </p>
            <p className="mt-2 text-[15px] leading-relaxed text-foreground">
              {q.explain}
            </p>
          </div>
        ) : null}
      </div>

      <div className="flex flex-wrap items-center justify-between gap-3">
        <Button variant="secondary" onClick={onPrev} disabled={id <= 1}>
          <ChevronLeft /> Anterior
        </Button>
        <div className="flex items-center gap-2">
          <Button
            variant={flagged ? "default" : "outline"}
            onClick={onFlag}
            aria-pressed={flagged}
          >
            <Bookmark className={flagged ? "fill-current" : undefined} />
            {flagged ? "Marcada" : "Marcar"}
          </Button>
          <Button onClick={onNext} disabled={id >= QUESTIONS.length}>
            Próxima <ChevronRight />
          </Button>
        </div>
      </div>

      {onJump ? (
        <ol className="grid grid-cols-10 gap-1.5">
          {QUESTIONS.map((item) => {
            const current = item.id === id;
            const answered = answeredIds?.includes(item.id);
            return (
              <li key={item.id}>
                <button
                  type="button"
                  onClick={() => onJump(item.id)}
                  className={cn(
                    "flex h-9 w-full items-center justify-center rounded-sm text-xs tabular-nums",
                    current
                      ? "bg-primary text-primary-foreground"
                      : answered
                        ? "bg-steel/15 text-ink"
                        : "bg-cream-deep text-muted-foreground hover:text-foreground",
                  )}
                  aria-label={`Ir para questão ${item.id}`}
                  aria-current={current ? "step" : undefined}
                >
                  {item.id}
                </button>
              </li>
            );
          })}
        </ol>
      ) : null}

      {footer}
    </article>
  );
}
