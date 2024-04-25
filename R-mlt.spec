#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: R
# autospec version: v10
# autospec commit: 5905be9
#
Name     : R-mlt
Version  : 1.5.1
Release  : 23
URL      : https://cran.r-project.org/src/contrib/mlt_1.5-1.tar.gz
Source0  : https://cran.r-project.org/src/contrib/mlt_1.5-1.tar.gz
Summary  : Most Likely Transformations
Group    : Development/Tools
License  : GPL-2.0
Requires: R-mlt-lib = %{version}-%{release}
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
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
models via the most likely transformation approach described in

%package lib
Summary: lib components for the R-mlt package.
Group: Libraries

%description lib
lib components for the R-mlt package.


%prep
%setup -q -n mlt
pushd ..
cp -a mlt buildavx2
popd
pushd ..
cp -a mlt buildavx512
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1713371630

%install
export SOURCE_DATE_EPOCH=1713371630
rm -rf %{buildroot}
LANG=C.UTF-8
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -flto -fno-semantic-interposition "
FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -flto -fno-semantic-interposition "
AR=gcc-ar
RANLIB=gcc-ranlib
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library
mkdir -p %{buildroot}-v3/usr/lib64/R/library
mkdir -p %{buildroot}-v4/usr/lib64/R/library
mkdir -p %{buildroot}-va/usr/lib64/R/library

mkdir -p ~/.R
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL  --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}-v3/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --preclean  --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}-v4/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean  --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :

/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}
/usr/bin/elf-move.py avx512 %{buildroot}-v4 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

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

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/R/library/mlt/libs/mlt.so
/V4/usr/lib64/R/library/mlt/libs/mlt.so
/usr/lib64/R/library/mlt/libs/mlt.so
