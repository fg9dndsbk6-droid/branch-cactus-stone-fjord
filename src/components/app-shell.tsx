import type { ReactNode } from "react";
import { Link, useRouterState } from "@tanstack/react-router";
import { FileDown } from "lucide-react";
import { cn } from "@/lib/utils";

const NAV = [
  { to: "/", label: "Início" },
  { to: "/praticar", label: "Praticar" },
  { to: "/simulado", label: "Simulado" },
  { to: "/revisao", label: "Revisão" },
];

export function AppShell({ children }: { children: ReactNode }) {
  const pathname = useRouterState({ select: (s) => s.location.pathname });

  return (
    <div className="min-h-dvh bg-background text-foreground">
      <a
        href="#conteudo"
        className="sr-only focus:not-sr-only focus:absolute focus:left-4 focus:top-4 focus:z-50 focus:rounded-md focus:bg-primary focus:px-3 focus:py-2 focus:text-primary-foreground"
      >
        Ir ao conteúdo
      </a>
      <header className="sticky top-0 z-40 border-b border-border bg-background/90 backdrop-blur-sm">
        <div className="mx-auto flex max-w-5xl items-center justify-between gap-3 px-4 py-3 sm:px-6">
          <Link to="/" className="flex min-w-0 items-baseline gap-2">
            <span className="font-display text-lg font-semibold tracking-tight text-ink">
              Epidemiologia
            </span>
            <span className="hidden truncate text-sm text-muted-foreground sm:inline">
              Aula 6 · Cássio Zini
            </span>
          </Link>
          <nav className="flex items-center gap-1" aria-label="Principal">
            {NAV.map((item) => {
              const active =
                item.to === "/"
                  ? pathname === "/"
                  : pathname.startsWith(item.to);
              return (
                <Link
                  key={item.to}
                  to={item.to}
                  className={cn(
                    "inline-flex h-11 items-center rounded-md px-3 text-sm font-medium transition-colors duration-[var(--motion-quick)]",
                    active
                      ? "bg-primary text-primary-foreground"
                      : "text-muted-foreground hover:bg-cream-deep hover:text-foreground",
                  )}
                >
                  {item.label}
                </Link>
              );
            })}
            <a
              href="/simulado-epidemiologia.pdf"
              download
              className="ml-1 inline-flex size-11 items-center justify-center rounded-md text-steel hover:bg-cream-deep"
              aria-label="Baixar PDF da lista"
            >
              <FileDown className="size-4" />
            </a>
          </nav>
        </div>
      </header>
      <main id="conteudo" className="mx-auto w-full max-w-5xl px-4 py-8 sm:px-6 sm:py-10">
        {children}
      </main>
    </div>
  );
}
