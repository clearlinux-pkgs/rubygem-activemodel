#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : rubygem-activemodel
Version  : 5.0.0
Release  : 13
URL      : https://rubygems.org/downloads/activemodel-5.0.0.gem
Source0  : https://rubygems.org/downloads/activemodel-5.0.0.gem
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
BuildRequires : ruby
BuildRequires : rubygem-rdoc

%description
= Active Model -- model interfaces for Rails
Active Model provides a known set of interfaces for usage in model classes.
They allow for Action Pack helpers to interact with non-Active Record models,
for example. Active Model also helps with building custom ORMs for use outside of
the Rails framework.

%prep
gem unpack %{SOURCE0}
%setup -q -D -T -n activemodel-5.0.0
gem spec %{SOURCE0} -l --ruby > rubygem-activemodel.gemspec

%build
export LANG=C
gem build rubygem-activemodel.gemspec

%install
%global gem_dir $(ruby -e'puts Gem.default_dir')
gem install -V \
--local \
--force \
--install-dir .%{gem_dir} \
--bindir .%{_bindir} \
activemodel-5.0.0.gem

mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
%{buildroot}%{gem_dir}

if [ -d .%{_bindir} ]; then
mkdir -p %{buildroot}%{_bindir}
cp -pa .%{_bindir}/* \
%{buildroot}%{_bindir}/
fi


%files
%defattr(-,root,root,-)
/usr/lib64/ruby/gems/2.3.0/cache/activemodel-5.0.0.gem
/usr/lib64/ruby/gems/2.3.0/gems/activemodel-5.0.0/CHANGELOG.md
/usr/lib64/ruby/gems/2.3.0/gems/activemodel-5.0.0/MIT-LICENSE
/usr/lib64/ruby/gems/2.3.0/gems/activemodel-5.0.0/README.rdoc
/usr/lib64/ruby/gems/2.3.0/gems/activemodel-5.0.0/lib/active_model.rb
/usr/lib64/ruby/gems/2.3.0/gems/activemodel-5.0.0/lib/active_model/attribute_assignment.rb
/usr/lib64/ruby/gems/2.3.0/gems/activemodel-5.0.0/lib/active_model/attribute_methods.rb
/usr/lib64/ruby/gems/2.3.0/gems/activemodel-5.0.0/lib/active_model/callbacks.rb
/usr/lib64/ruby/gems/2.3.0/gems/activemodel-5.0.0/lib/active_model/conversion.rb
/usr/lib64/ruby/gems/2.3.0/gems/activemodel-5.0.0/lib/active_model/dirty.rb
/usr/lib64/ruby/gems/2.3.0/gems/activemodel-5.0.0/lib/active_model/errors.rb
/usr/lib64/ruby/gems/2.3.0/gems/activemodel-5.0.0/lib/active_model/forbidden_attributes_protection.rb
/usr/lib64/ruby/gems/2.3.0/gems/activemodel-5.0.0/lib/active_model/gem_version.rb
/usr/lib64/ruby/gems/2.3.0/gems/activemodel-5.0.0/lib/active_model/lint.rb
/usr/lib64/ruby/gems/2.3.0/gems/activemodel-5.0.0/lib/active_model/locale/en.yml
/usr/lib64/ruby/gems/2.3.0/gems/activemodel-5.0.0/lib/active_model/model.rb
/usr/lib64/ruby/gems/2.3.0/gems/activemodel-5.0.0/lib/active_model/naming.rb
/usr/lib64/ruby/gems/2.3.0/gems/activemodel-5.0.0/lib/active_model/railtie.rb
/usr/lib64/ruby/gems/2.3.0/gems/activemodel-5.0.0/lib/active_model/secure_password.rb
/usr/lib64/ruby/gems/2.3.0/gems/activemodel-5.0.0/lib/active_model/serialization.rb
/usr/lib64/ruby/gems/2.3.0/gems/activemodel-5.0.0/lib/active_model/serializers/json.rb
/usr/lib64/ruby/gems/2.3.0/gems/activemodel-5.0.0/lib/active_model/test_case.rb
/usr/lib64/ruby/gems/2.3.0/gems/activemodel-5.0.0/lib/active_model/translation.rb
/usr/lib64/ruby/gems/2.3.0/gems/activemodel-5.0.0/lib/active_model/type.rb
/usr/lib64/ruby/gems/2.3.0/gems/activemodel-5.0.0/lib/active_model/type/big_integer.rb
/usr/lib64/ruby/gems/2.3.0/gems/activemodel-5.0.0/lib/active_model/type/binary.rb
/usr/lib64/ruby/gems/2.3.0/gems/activemodel-5.0.0/lib/active_model/type/boolean.rb
/usr/lib64/ruby/gems/2.3.0/gems/activemodel-5.0.0/lib/active_model/type/date.rb
/usr/lib64/ruby/gems/2.3.0/gems/activemodel-5.0.0/lib/active_model/type/date_time.rb
/usr/lib64/ruby/gems/2.3.0/gems/activemodel-5.0.0/lib/active_model/type/decimal.rb
/usr/lib64/ruby/gems/2.3.0/gems/activemodel-5.0.0/lib/active_model/type/decimal_without_scale.rb
/usr/lib64/ruby/gems/2.3.0/gems/activemodel-5.0.0/lib/active_model/type/float.rb
/usr/lib64/ruby/gems/2.3.0/gems/activemodel-5.0.0/lib/active_model/type/helpers.rb
/usr/lib64/ruby/gems/2.3.0/gems/activemodel-5.0.0/lib/active_model/type/helpers/accepts_multiparameter_time.rb
/usr/lib64/ruby/gems/2.3.0/gems/activemodel-5.0.0/lib/active_model/type/helpers/mutable.rb
/usr/lib64/ruby/gems/2.3.0/gems/activemodel-5.0.0/lib/active_model/type/helpers/numeric.rb
/usr/lib64/ruby/gems/2.3.0/gems/activemodel-5.0.0/lib/active_model/type/helpers/time_value.rb
/usr/lib64/ruby/gems/2.3.0/gems/activemodel-5.0.0/lib/active_model/type/immutable_string.rb
/usr/lib64/ruby/gems/2.3.0/gems/activemodel-5.0.0/lib/active_model/type/integer.rb
/usr/lib64/ruby/gems/2.3.0/gems/activemodel-5.0.0/lib/active_model/type/registry.rb
/usr/lib64/ruby/gems/2.3.0/gems/activemodel-5.0.0/lib/active_model/type/string.rb
/usr/lib64/ruby/gems/2.3.0/gems/activemodel-5.0.0/lib/active_model/type/text.rb
/usr/lib64/ruby/gems/2.3.0/gems/activemodel-5.0.0/lib/active_model/type/time.rb
/usr/lib64/ruby/gems/2.3.0/gems/activemodel-5.0.0/lib/active_model/type/unsigned_integer.rb
/usr/lib64/ruby/gems/2.3.0/gems/activemodel-5.0.0/lib/active_model/type/value.rb
/usr/lib64/ruby/gems/2.3.0/gems/activemodel-5.0.0/lib/active_model/validations.rb
/usr/lib64/ruby/gems/2.3.0/gems/activemodel-5.0.0/lib/active_model/validations/absence.rb
/usr/lib64/ruby/gems/2.3.0/gems/activemodel-5.0.0/lib/active_model/validations/acceptance.rb
/usr/lib64/ruby/gems/2.3.0/gems/activemodel-5.0.0/lib/active_model/validations/callbacks.rb
/usr/lib64/ruby/gems/2.3.0/gems/activemodel-5.0.0/lib/active_model/validations/clusivity.rb
/usr/lib64/ruby/gems/2.3.0/gems/activemodel-5.0.0/lib/active_model/validations/confirmation.rb
/usr/lib64/ruby/gems/2.3.0/gems/activemodel-5.0.0/lib/active_model/validations/exclusion.rb
/usr/lib64/ruby/gems/2.3.0/gems/activemodel-5.0.0/lib/active_model/validations/format.rb
/usr/lib64/ruby/gems/2.3.0/gems/activemodel-5.0.0/lib/active_model/validations/helper_methods.rb
/usr/lib64/ruby/gems/2.3.0/gems/activemodel-5.0.0/lib/active_model/validations/inclusion.rb
/usr/lib64/ruby/gems/2.3.0/gems/activemodel-5.0.0/lib/active_model/validations/length.rb
/usr/lib64/ruby/gems/2.3.0/gems/activemodel-5.0.0/lib/active_model/validations/numericality.rb
/usr/lib64/ruby/gems/2.3.0/gems/activemodel-5.0.0/lib/active_model/validations/presence.rb
/usr/lib64/ruby/gems/2.3.0/gems/activemodel-5.0.0/lib/active_model/validations/validates.rb
/usr/lib64/ruby/gems/2.3.0/gems/activemodel-5.0.0/lib/active_model/validations/with.rb
/usr/lib64/ruby/gems/2.3.0/gems/activemodel-5.0.0/lib/active_model/validator.rb
/usr/lib64/ruby/gems/2.3.0/gems/activemodel-5.0.0/lib/active_model/version.rb
/usr/lib64/ruby/gems/2.3.0/specifications/activemodel-5.0.0.gemspec
