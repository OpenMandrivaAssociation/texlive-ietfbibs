%global tl_name ietfbibs
%global tl_revision 41332

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0.0
Release:	%{tl_revision}.1
Summary:	Generate BibTeX entries for various IETF index files
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/biblio/bibtex/utils/ietfbibs
License:	mit
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/ietfbibs.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/ietfbibs.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides scripts to translate IETF index files to BibTeX
files.

