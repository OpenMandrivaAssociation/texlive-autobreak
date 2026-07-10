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
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package implements a simple mechanism of line/page breaking within
the align environment of the amsmath package; new line characters are
considered as possible candidates for the breaks and the package tries
to put breaks at adequate places. It is suitable for computer-generated
long formulae with many terms.

%prep
%setup -q -c -a1 -a2
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/source
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/latex
%dir %{_datadir}/texmf-dist/source/latex
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/doc/latex/autobreak
%dir %{_datadir}/texmf-dist/source/latex/autobreak
%dir %{_datadir}/texmf-dist/tex/latex/autobreak
%doc %{_datadir}/texmf-dist/doc/latex/autobreak/README.md
%doc %{_datadir}/texmf-dist/doc/latex/autobreak/autobreak.pdf
%doc %{_datadir}/texmf-dist/source/latex/autobreak/autobreak.dtx
%doc %{_datadir}/texmf-dist/source/latex/autobreak/autobreak.ins
%{_datadir}/texmf-dist/tex/latex/autobreak/autobreak.sty
