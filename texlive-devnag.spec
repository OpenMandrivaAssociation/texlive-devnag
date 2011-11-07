# revision 18835
# category TLCore
# catalog-ctan /language/devanagari/velthuis
# catalog-date 2008-06-22 18:57:24 +0200
# catalog-license gpl
# catalog-version 2.15
Name:		texlive-devnag
Version:	2.15
Release:	1
Summary:	Typeset Devanagari
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/language/devanagari/velthuis
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/devnag.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires:	texlive-devnag.bin
Conflicts:	texlive-texmf <= 20110705-3

%description
Frans Velthuis' preprocessor for Devanagari text, and fonts and
macros to use when typesetting the processed text. The macros
provide features that support Sanskrit, Hindi, Marathi, Nepali,
and other languages typically printed in the Devanagari script.
The fonts are available both in Metafont and Type 1 format.

#-----------------------------------------------------------------------
%files
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0

%build

%install
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
