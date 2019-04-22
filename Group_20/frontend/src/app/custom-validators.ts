import { ValidatorFn, AbstractControl } from '@angular/forms';

export function nameValidator(): ValidatorFn {
  return (control: AbstractControl): {[key: string]: any} | null => {
    const forbidden = /[^A-Za-z]/i.test(control.value);
    return forbidden ? {'nameValidator': control.value}: null;
  };
}
export function resnameValidator(): ValidatorFn {
  return (control: AbstractControl): {[key: string]: any} | null => {
    const forbidden = /[^ A-Za-z]/i.test(control.value);
    return forbidden ? {'resnameValidator': control.value}: null;
  };
}
export function descriptionValidator(): ValidatorFn {
  return (control: AbstractControl): {[key: string]: any} | null => {
    const forbidden = /[^ .A-Za-z]/i.test(control.value);
    return forbidden ? {'resnameValidator': control.value}: null;
  };
}
export function phoneValidator(): ValidatorFn {
  return (control: AbstractControl): {[key: string]: any} | null => {
    const forbidden = /[0-9]{10}/i.test(control.value) && control.value.length === 10;
    return forbidden ? null: {'phoneValidator': control.value};
  };
}
export function priceValidator(): ValidatorFn {
  return (control: AbstractControl): {[key: string]: any} | null => {
    const forbidden = /[^0-9]/i.test(control.value)
    return forbidden ? {'priceValidator': control.value} : null; 
  };
}
export function zipcodeValidator(): ValidatorFn {
  return (control: AbstractControl): {[key: string]: any} | null => {
    const forbidden = /[1-9][0-9][0-9][0-9][0-9][0-9]/i.test(control.value)
    return forbidden ? null: {'zipcodeValidator': control.value};
  };
}
export function timeValidator(): ValidatorFn {
  return (control: AbstractControl): {[key: string]: any} | null => {
    const forbidden = /[0-1][0-9][0-5][0-9]/i.test(control.value) || /[2][0-3][0-5][0-9]/i.test(control.value)
    return forbidden ? null: {'timeValidator': control.value};
  };
}
export function addressValidator(): ValidatorFn {
  return (control: AbstractControl): {[key: string]: any} | null => {
    const forbidden = /[a-zA-Z0-9]+[\s]*[a-zA-Z0-9.\-\,\#]+[\s]*[a-zA-Z0-9.\-\,\#]+[a-zA-Z0-9\s.\-\,\#]*/i.test(control.value)
    return forbidden ? null: {'addressValidator': control.value};
  };
}
export function emailValidator(): ValidatorFn {
  return (control: AbstractControl): {[key: string]: any} | null => {
    const forbidden = /([a-zA-Z0-9_\-\.]+)@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.)|(([a-zA-Z0-9\-]+\.)+))([a-zA-Z]{2,4}|[0-9]{1,3})(\]?)/i.test(control.value);
    return forbidden ? null: {'emailValidator': control.value};
  };
}
export function usernameValidator(): ValidatorFn {
  return (control: AbstractControl): {[key: string]: any} | null => {
    if(/[a-zA-Z0-9][a-zA-Z0-9_.]{2,29}/i.test(control.value)){
      if(/^(?!restaurant).+/i.test(control.value)){
        return null;
      } else {
        return {'usernameAvailableValidator': control.value}
      }
    } else{ 
      return {'usernameValidator': control.value}
    }
  };
}
/[0-9a-zA-Z]{6,}/i
export function passwordValidator(): ValidatorFn {
  return (control: AbstractControl): {[key: string]: any} | null => {
    const num = /[0-9]/i.test(control.value);
    const char = /[a-zA-Z]/i.test(control.value);
    var out = {};
    if (!/[0-9]/i.test(control.value)){
      out['passwordNumValidator'] = true;
    }
    if(!/[a-zA-Z]/i.test(control.value)){
      out['passwordCharValidator'] = true
    }
    if (control.value.length < 6){
      out['passwordLenValidator'] = true
    }
    console.log(out);
    return out ? out: null;
  };
}

export function matchOtherValidator (otherControlName: string) {

  let thisControl: AbstractControl;
  let otherControl: AbstractControl;

  return function matchOtherValidate (control: AbstractControl) {

    if (!control.parent) {
      return null;
    }

    // Initializing the validator.
    if (!thisControl) {
      thisControl = control;
      otherControl = control.parent.get(otherControlName) as AbstractControl;
      if (!otherControl) {
        throw new Error('matchOtherValidator(): other control is not found in parent group');
      }
      otherControl.valueChanges.subscribe(() => {
        thisControl.updateValueAndValidity();
      });
    }

    if (!otherControl) {
      return null;
    }

    if (otherControl.value !== thisControl.value) {
      return {
        matchOtherValidator: true
      };
    }

    return null;

  }

}
