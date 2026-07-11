%global tl_name autobreak
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.3
Release:	%{tl_revision}.1
Summary:	Simple line breaking of long formulae
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/autobreak
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/autobreak.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/autobreak.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/autobreak.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package implements a simple mechanism of line/page breaking within
the align environment of the amsmath package; new line characters are
considered as possible candidates for the breaks and the package tries
to put breaks at adequate places. It is suitable for computer-generated
long formulae with many terms.

