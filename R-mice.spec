#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-mice
Version  : 3.13.0
Release  : 9
URL      : https://cran.r-project.org/src/contrib/mice_3.13.0.tar.gz
Source0  : https://cran.r-project.org/src/contrib/mice_3.13.0.tar.gz
Summary  : Multivariate Imputation by Chained Equations
Group    : Development/Tools
License  : GPL-2.0 GPL-3.0
Requires: R-mice-lib = %{version}-%{release}
Requires: R-Rcpp
Requires: R-broom
Requires: R-cpp11
Requires: R-dplyr
Requires: R-generics
Requires: R-rlang
Requires: R-tidyr
BuildRequires : R-Rcpp
BuildRequires : R-broom
BuildRequires : R-cpp11
BuildRequires : R-dplyr
BuildRequires : R-generics
BuildRequires : R-metafor
BuildRequires : R-rlang
BuildRequires : R-tidyr
BuildRequires : buildreq-R

%description
implemented by the MICE algorithm as described in Van Buuren and

%package lib
Summary: lib components for the R-mice package.
Group: Libraries

%description lib
lib components for the R-mice package.


%prep
%setup -q -c -n mice
cd %{_builddir}/mice

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1611862533

%install
export SOURCE_DATE_EPOCH=1611862533
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
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library mice
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library mice
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library mice
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc mice || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/mice/CITATION
/usr/lib64/R/library/mice/DESCRIPTION
/usr/lib64/R/library/mice/INDEX
/usr/lib64/R/library/mice/Meta/Rd.rds
/usr/lib64/R/library/mice/Meta/data.rds
/usr/lib64/R/library/mice/Meta/features.rds
/usr/lib64/R/library/mice/Meta/hsearch.rds
/usr/lib64/R/library/mice/Meta/links.rds
/usr/lib64/R/library/mice/Meta/nsInfo.rds
/usr/lib64/R/library/mice/Meta/package.rds
/usr/lib64/R/library/mice/NAMESPACE
/usr/lib64/R/library/mice/NEWS.md
/usr/lib64/R/library/mice/R/mice
/usr/lib64/R/library/mice/R/mice.rdb
/usr/lib64/R/library/mice/R/mice.rdx
/usr/lib64/R/library/mice/data/Rdata.rdb
/usr/lib64/R/library/mice/data/Rdata.rds
/usr/lib64/R/library/mice/data/Rdata.rdx
/usr/lib64/R/library/mice/help/AnIndex
/usr/lib64/R/library/mice/help/aliases.rds
/usr/lib64/R/library/mice/help/mice.rdb
/usr/lib64/R/library/mice/help/mice.rdx
/usr/lib64/R/library/mice/help/paths.rds
/usr/lib64/R/library/mice/html/00Index.html
/usr/lib64/R/library/mice/html/R.css
/usr/lib64/R/library/mice/tests/testthat.R
/usr/lib64/R/library/mice/tests/testthat/test-D1.R
/usr/lib64/R/library/mice/tests/testthat/test-D3.R
/usr/lib64/R/library/mice/tests/testthat/test-ampute.R
/usr/lib64/R/library/mice/tests/testthat/test-anova.R
/usr/lib64/R/library/mice/tests/testthat/test-as.mids.R
/usr/lib64/R/library/mice/tests/testthat/test-blocks.R
/usr/lib64/R/library/mice/tests/testthat/test-blots.R
/usr/lib64/R/library/mice/tests/testthat/test-cbind.R
/usr/lib64/R/library/mice/tests/testthat/test-check.formula.R
/usr/lib64/R/library/mice/tests/testthat/test-check.visitSequence.R
/usr/lib64/R/library/mice/tests/testthat/test-complete.R
/usr/lib64/R/library/mice/tests/testthat/test-filter.R
/usr/lib64/R/library/mice/tests/testthat/test-formulas.R
/usr/lib64/R/library/mice/tests/testthat/test-loggedEvents.R
/usr/lib64/R/library/mice/tests/testthat/test-make.predictorMatrix.R
/usr/lib64/R/library/mice/tests/testthat/test-md.pattern.R
/usr/lib64/R/library/mice/tests/testthat/test-mice-initialize.R
/usr/lib64/R/library/mice/tests/testthat/test-mice.R
/usr/lib64/R/library/mice/tests/testthat/test-mice.impute.2l.bin.R
/usr/lib64/R/library/mice/tests/testthat/test-mice.impute.2l.lmer.R
/usr/lib64/R/library/mice/tests/testthat/test-mice.impute.2l.norm.R
/usr/lib64/R/library/mice/tests/testthat/test-mice.impute.2lonly.mean.R
/usr/lib64/R/library/mice/tests/testthat/test-mice.impute.2lonly.norm.R
/usr/lib64/R/library/mice/tests/testthat/test-mice.impute.jomoImpute.R
/usr/lib64/R/library/mice/tests/testthat/test-mice.impute.norm.R
/usr/lib64/R/library/mice/tests/testthat/test-mice.impute.panImpute.R
/usr/lib64/R/library/mice/tests/testthat/test-mice.impute.pmm.R
/usr/lib64/R/library/mice/tests/testthat/test-mice.impute.polr.R
/usr/lib64/R/library/mice/tests/testthat/test-mira.R
/usr/lib64/R/library/mice/tests/testthat/test-newdata.R
/usr/lib64/R/library/mice/tests/testthat/test-parlmice.R
/usr/lib64/R/library/mice/tests/testthat/test-pool.R
/usr/lib64/R/library/mice/tests/testthat/test-pool.r.squared.R
/usr/lib64/R/library/mice/tests/testthat/test-rbind.R
/usr/lib64/R/library/mice/tests/testthat/test-remove.lindep.R
/usr/lib64/R/library/mice/tests/testthat/test-tidiers.R
/usr/lib64/R/library/mice/tests/testthat/test-update.design.R
/usr/lib64/R/library/mice/tests/testthat/test-with.R

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/mice/libs/mice.so
