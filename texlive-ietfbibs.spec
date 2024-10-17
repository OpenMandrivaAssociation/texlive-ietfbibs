Name:		texlive-ietfbibs
Version:	41332
Release:	2
Summary:	Generate BibTeX entries for various IETF index files
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/ietfbibs
License:	mit
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ietfbibs.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ietfbibs.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides scripts to translate IETF index files to
BibTeX files.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/doc/bibtex/ietfbibs

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
