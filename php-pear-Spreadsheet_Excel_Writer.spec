%include	/usr/lib/rpm/macros.php
%define         _class          Spreadsheet
%define         _subclass       Excel
%define		_status		beta

%define		_pearname	%{_class}_%{_subclass}_Writer
Summary:	%{_pearname} - Package for generating Excel spreadsheets
Summary(pl):	%{_pearname} - pakiet generuj±cy arkusze Excela
Name:		php-pear-%{_pearname}
Version:	0.3
Release:	1
License:	LGPL
Group:		Development/Languages/PHP
# Source0-md5:	32bffe9fa7f7a56bebc0e5f78164f366
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
URL:		http://pear.php.net/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Spreadsheet_Excel_Writer was born as a porting of the
Spreadsheet::WriteExcel Perl module to PHP. It allows writing of Excel
spreadsheets without the need for COM objects. It supports formulas,
images (BMP) and all kinds of formatting for text and cells. It
currently supports the BIFF5 format (Excel 5.0), so functionality
appeared in the latest Excel versions is not yet available.

This class has in PEAR status: %{_status}.

%description -l pl
Spreadsheet_Excel_Writer narodzi³ siê jako port do PHP perlowego
modu³u Spreadsheet::WriteExcel. Pozwala na zapisywanie arkuszy Excela
bez potrzeby u¿ywania obiektów COM. Ma wsparcie dla formularzy,
rysunków (BMP) oraz wszelkiego typu formatowania tekstu oraz komórek.
Aktualnie wspiera format BIFF5 (Excel 5.0), wiêc funkcjonalno¶æ
ostatnich wersji Excela nie jest jeszcze dostêpna.

Ta klasa ma w PEAR status: %{_status}.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}/Writer

install %{_pearname}-%{version}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}
install %{_pearname}-%{version}/Writer/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}/Writer/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{php_pear_dir}/%{_class}/
%dir %{php_pear_dir}/%{_class}/%{_subclass}
%dir %{php_pear_dir}/%{_class}/%{_subclass}/Writer
%{php_pear_dir}/%{_class}/%{_subclass}/*.php
%{php_pear_dir}/%{_class}/%{_subclass}/Writer/*.php
