import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class PasswordValidatorTest {

    private final PasswordValidator validator = new PasswordValidator();

    @Test
    void isValid_validPassword_returnsTrue() {
        assertTrue(validator.isValid("ValidPass123"));
    }

    @Test
    void isValid_shortPassword_returnsFalse() {
        assertFalse(validator.isValid("Short"));
    }

    @Test
    void isValid_noUppercase_returnsFalse() {
        assertFalse(validator.isValid("nopassword"));
    }

    @Test
    void isValid_noLowercase_returnsFalse() {
        assertFalse(validator.isValid("PASSWORD123"));
    }

    @Test
    void isValid_noDigit_returnsFalse() {
        assertFalse(validator.isValid("NoDigitPassword"));
    }

    @Test
    void isValid_specialCharacter_returnsTrue() {
      assertTrue(validator.isValid("ValidPass!123"));
    }

    @Test
    void isValid_longPassword_returnsTrue() {
        assertTrue(validator.isValid("ThisPasswordIsValid123!"));
    }
}

class PasswordValidator {
    public boolean isValid(String password) {
        if (password == null || password.length() < 8) {
            return false;
        }

        boolean hasUppercase = false;
        boolean hasLowercase = false;
        boolean hasDigit = false;

        for (char c : password.toCharArray()) {
            if (Character.isUpperCase(c)) {
                hasUppercase = true;
            } else if (Character.isLowerCase(c)) {
                hasLowercase = true;
            } else if (Character.isDigit(c)) {
                hasDigit = true;
            }
        }

        return hasUppercase && hasLowercase && hasDigit;
    }
}