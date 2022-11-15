Name:		texlive-autobreak
Version:	43337
Release:	1
Summary:	Simple line breaking of long formulae
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/autobreak
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/autobreak.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/autobreak.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/autobreak.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package implements a simple mechanism of line/page
breaking within the align environment of the amsmath package;
new line characters are considered as possible candidates for
the breaks and the package tries to put breaks at adequate
places. It is suitable for computer-generated long formulae
with many terms.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/autobreak
%{_texmfdistdir}/tex/latex/autobreak
%doc %{_texmfdistdir}/doc/latex/autobreak

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
