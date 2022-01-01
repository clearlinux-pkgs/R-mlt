#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-mlt
Version  : 1.3.2
Release  : 3
URL      : https://cran.r-project.org/src/contrib/mlt_1.3-2.tar.gz
Source0  : https://cran.r-project.org/src/contrib/mlt_1.3-2.tar.gz
Summary  : Most Likely Transformations
Group    : Development/Tools
License  : GPL-2.0
Requires: R-BB
Requires: R-alabama
Requires: R-basefun
Requires: R-coneproj
Requires: R-nloptr
Requires: R-numDeriv
Requires: R-sandwich
Requires: R-variables
BuildRequires : R-BB
BuildRequires : R-TH.data
BuildRequires : R-alabama
BuildRequires : R-basefun
BuildRequires : R-coneproj
BuildRequires : R-nloptr
BuildRequires : R-numDeriv
BuildRequires : R-sandwich
BuildRequires : R-variables
BuildRequires : buildreq-R

%description
models via the most likely transformation approach described in

%prep
%setup -q -c -n mlt
cd %{_builddir}/mlt

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1641062025

%install
export SOURCE_DATE_EPOCH=1641062025
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library mlt
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library mlt
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library mlt
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc mlt || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/mlt/CITATION
/usr/lib64/R/library/mlt/DESCRIPTION
/usr/lib64/R/library/mlt/INDEX
/usr/lib64/R/library/mlt/Meta/Rd.rds
/usr/lib64/R/library/mlt/Meta/features.rds
/usr/lib64/R/library/mlt/Meta/hsearch.rds
/usr/lib64/R/library/mlt/Meta/links.rds
/usr/lib64/R/library/mlt/Meta/nsInfo.rds
/usr/lib64/R/library/mlt/Meta/package.rds
/usr/lib64/R/library/mlt/NAMESPACE
/usr/lib64/R/library/mlt/NEWS.Rd
/usr/lib64/R/library/mlt/R/mlt
/usr/lib64/R/library/mlt/R/mlt.rdb
/usr/lib64/R/library/mlt/R/mlt.rdx
/usr/lib64/R/library/mlt/help/AnIndex
/usr/lib64/R/library/mlt/help/aliases.rds
/usr/lib64/R/library/mlt/help/mlt.rdb
/usr/lib64/R/library/mlt/help/mlt.rdx
/usr/lib64/R/library/mlt/help/paths.rds
/usr/lib64/R/library/mlt/html/00Index.html
/usr/lib64/R/library/mlt/html/R.css
/usr/lib64/R/library/mlt/tests/2sample.R
/usr/lib64/R/library/mlt/tests/2sample.Rout.save
/usr/lib64/R/library/mlt/tests/Cox-Ex.R
/usr/lib64/R/library/mlt/tests/Cox-Ex.Rout.save
/usr/lib64/R/library/mlt/tests/bugfixes.R
/usr/lib64/R/library/mlt/tests/bugfixes.Rout.save
/usr/lib64/R/library/mlt/tests/distr-Ex.R
/usr/lib64/R/library/mlt/tests/dpq-Ex.R
/usr/lib64/R/library/mlt/tests/dpq-Ex.Rout.save
/usr/lib64/R/library/mlt/tests/glm-Ex.R
/usr/lib64/R/library/mlt/tests/glm-Ex.Rout.save
/usr/lib64/R/library/mlt/tests/lm-Ex.R
/usr/lib64/R/library/mlt/tests/lm-Ex.Rout.save
/usr/lib64/R/library/mlt/tests/polr-Ex.R
/usr/lib64/R/library/mlt/tests/polr-Ex.Rout.save
/usr/lib64/R/library/mlt/tests/predict-Ex.R
/usr/lib64/R/library/mlt/tests/predict-Ex.Rout.save
/usr/lib64/R/library/mlt/tests/subset.R
/usr/lib64/R/library/mlt/tests/subset.Rout.save
/usr/lib64/R/library/mlt/tests/surv-Ex.R
/usr/lib64/R/library/mlt/tests/surv-Ex.Rout.save
