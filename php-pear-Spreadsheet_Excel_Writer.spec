%define		_status		beta
%define		_pearname	Spreadsheet_Excel_Writer
Summary:	%{_pearname} - package for generating Excel spreadsheets
Summary(pl.UTF-8):	%{_pearname} - pakiet generujący arkusze Excela
Name:		php-pear-%{_pearname}
Version:	0.9.4
Release:	1
License:	LGPL
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	ac3355bd8c5eddac6b1feee78a7fe5c6
URL:		http://pear.php.net/package/Spreadsheet_Excel_Writer/
BuildRequires:	php-pear-PEAR >= 1:1.4.0-0.b1
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php(core) >= 4.1.0
Requires:	php-pear
Requires:	php-pear-OLE >= 0.5
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Spreadsheet_Excel_Writer was born as a porting of the
Spreadsheet::WriteExcel Perl module to PHP. It allows writing of Excel
spreadsheets without the need for COM objects. It supports formulas,
images (BMP) and all kinds of formatting for text and cells. It
currently supports the BIFF5 format (Excel 5.0), so functionality
appeared in the latest Excel versions is not yet available.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Spreadsheet_Excel_Writer narodził się jako port do PHP perlowego
modułu Spreadsheet::WriteExcel. Pozwala na zapisywanie arkuszy Excela
bez potrzeby używania obiektów COM. Ma wsparcie dla formularzy,
rysunków (BMP) oraz wszelkiego typu formatowania tekstu oraz komórek.
Aktualnie wspiera format BIFF5 (Excel 5.0), więc funkcjonalność
ostatnich wersji Excela nie jest jeszcze dostępna.

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%dir %{php_pear_dir}/Spreadsheet
%dir %{php_pear_dir}/Spreadsheet/Excel
%dir %{php_pear_dir}/Spreadsheet/Excel/Writer
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/Spreadsheet/Excel/*.php
%{php_pear_dir}/Spreadsheet/Excel/Writer/*.php
