%Introduzione alla Classe miaclasse

%...%

%compilatore da usare
\NeedsTeXFormat{LaTeX2e}
%nome della classe che sto creando
\ProvidesClass{miaclasse}[2023/11/24 Classe LaTeX per le mie robe, basata su report] 
%"miaclasse" in ProvidesClass è il percorso in cui trova si trova il file

%...%


%va messo dopo le opzioni, nel caso di book le opzioni sono la dimensione testo e oneside, nel miaclasse non ho opzioni
\ProcessOptions\relax 
\LoadClass{report} %classe di partenza


%...%


%pacchetti che servono per definire nuovi comandi
\RequirePackage{mathtools}
%\RequirePackage{amssymb} %da usare per \cap
%\RequirePackage{graphicx}
%\RequirePackage{color}
%pacchetto per modificare stili capitoli, sezioni, ecc
\RequirePackage{titlesec}
\RequirePackage[italian]{babel}
\RequirePackage[useregional = text]{datetime2}
\RequirePackage{fancyhdr}   %% serve per avere headers e footers



%...%


%nuovi comandi
%\newcommand*{\vettore}[1]{\underline{#1}}
%\newcommand*{\vettorederivata}[1]{\underline{\Dot{#1}}}
%\newcommand*{\versore}[1]{\hat{#1}}
%\newcommand*{\derivata}[2]{\frac{d#1}{d#2}}
%\newcommand*{\derivataparz}[2]{\frac{\partial #1}{\partial #2}}
\newcommand*{\VelAng}{\dot{\theta}}
\newcommand*{\AccAng}{\Ddot{\theta}}
%\newcommand*{\accelerazione}[1]{\Ddot{#1}}
%\newcommand*{\angolo}[1]{\widehat{#1}}
%\newcommand*{\intersecato}{\cap}
%\newcommand*{\unito}{\cup}
%\newcommand*{\integrale}[4]{\int_{#1}^{#2} #3 d(#4)}
%\newcommand*{\unitamisura}[2]{\left[\frac{\textup#1}{\textup#2}\right]}
\newcommand*{\mezzo}{\frac{1}{2}}
%\newcommand*{\celsius}{^{\circ} \mathrm{C}}
%\newcommand*{\vettore}[1]{\vec{#1}}
%\newcommand*{\vettorederivata}[1]{\underline{\Dot{#1}}}
%\newcommand*{\versore}[1]{\hat{#1}}
\newcommand*{\derivata}[2]{\frac{d#1}{d#2}}
\newcommand*{\derivataparz}[2]{\frac{\partial #1}{\partial #2}}
%\newcommand*{\accelerazione}[1]{\Ddot{#1}}
% \newcommand*{\angolo}[1]{\widehat{#1}}
% \newcommand*{\intersecato}{\cap}
% \newcommand*{\unito}{\cup}
% \newcommand*{\integrale}[4]{\int_{#1}^{#2} #3 d(#4)}
% \newcommand*{\unitamisura}[2]{\left[\frac{\textup#1}{\textup#2}\right]}
% \newcommand*{\Pa}{\left[\textup{Pa}\right]}
% \newcommand*{\abs}[1]{\left|#1\right|}
% \newcommand*{\cost}{\textup{cost}}

%\newcommand*{\roma}[1]{\expandafter\@slowromancap\romannumeral #1@}


%geometria pagina
\RequirePackage[a4paper,width=16.5cm,top=2.5cm,bottom=2.5cm]{geometry}
%\RequirePackage[a4paper]{geometry}


%....%
% Define title and author
\newcommand{\@titolo}{}
\newcommand{\@autore}{}

% Set title and author
\newcommand{\titolo}[1]{\renewcommand{\@titolo}{#1}}
\newcommand{\autore}[1]{\renewcommand{\@autore}{#1}}

%comando \primapag per titolo in prima pagina
\newcommand{\primapag}	{
    { \centering{\Huge\textsc{\@titolo}}\par %titolo
		\vspace{1cm}
    {\Large \textit{\@autore}} \par %autore
    		\vspace{1.5cm} 
    \includegraphics[width=0.3\textwidth]{Immagini/Univi.jpg} %iconcina università
    		\vfill %vado fino in fondo
    \centering\textsf{\today}\par } %data
  {\thispagestyle{empty}} } %questo comando serve per non mettere il numerino della pagina anche sul foglio del titolo


%...%

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%% Stile pagina
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Configure fancyhdr
\pagestyle{fancy}
\makeatletter
\fancyhf{} % Clear header and footer
\lhead{\@titolo}
\rhead{Pagina \thepage}
\lfoot{\@autore}
\rfoot{Anno Scolastico 2023/2024}
\renewcommand{\footrulewidth}{0.3pt}
\renewcommand{\headrulewidth}{0.3pt}
\makeatother 

%formattazione capitoli, sezioni, paragrafi


%....%


%cambio di stile di capitoli, sezioni, ecc

\input{ArtNouvc.fd} %font usato per numero capitolo


\titleformat{\chapter}{\normalfont\huge\scshape}{\usefont{U}{ArtNouvc}{xl}{n}\thechapter}{1ex}{\huge}
%\titleformat*{\chapter}{\normalfont\huge\scshape}{\thechapter}{1ex}{\huge}
\titleformat{\section}{\normalfont\Large\bfseries}{\thesection}{1ex}{\Large}
\titleformat{\subsection}{\normalfont\large\bfseries}{\thesubsection}{1ex}{\large}
\titleformat{\subsubsection}{\normalfont\normalsize\bfseries}{\thesubsubsection}{1ex}{\normalsize}
\titleformat{\paragraph}[runin]{\normalfont\normalsize\bfseries}{\theparagraph}{1ex}{\normalsize}
\titleformat{\subparagraph}[runin]{\normalfont\normalsize\bfseries}{\thesubparagraph}{1ex}{\normalsize}
\titlespacing*{\chapter}{0pt}{0pt}{0.75cm}
\titlespacing*{\section}{0pt}{0.5cm}{0.35cm} %{3.5ex plus 1ex minus .2ex}{2.3ex plus .2ex}
\titlespacing*{\subsection}{0pt}{0.25cm}{0.15cm} %{3.25ex plus 1ex minus .2ex}{1.5ex plus .2ex}
\titlespacing*{\subsubsection}{0pt}{1.5mm}{1.5mm}%{3.25ex plus 1ex minus .2ex}{1.5ex plus .2ex}
\titlespacing*{\paragraph}{0pt}{0.5mm}{0.5mm}%{3.25ex plus 1ex minus .2ex}{1em}
\titlespacing*{\subparagraph}{\parindent}{0.25mm}{0.25mm}%{3.25ex plus 1ex minus .2ex}{1em}


%...%


\newcommand*{\capitolo}[1]{\chapter{#1}}
\newcommand*{\sezione}[1]{\section{#1}}
\newcommand*{\sottosezione}[1]{\subsection{#1}}
\newcommand*{\sottosottosezione}[1]{\subsubsection{#1}}
\newcommand*{\paragrafo}[1]{\paragraph{#1}\mbox{}}
\newcommand*{\sottoparagrafo}[1]{\subparagraph{#1}\mbox{}}



%...%

\endinput