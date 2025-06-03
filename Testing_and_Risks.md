# Testing and Risks

## Testing Plan

- **Functional Testing**: Ensure each scenario works and provides correct feedback.
- **Usability Testing**: Main menu, buttons, text boxes are clear and easy.
- **Edge Cases**: Empty name, long names, replaying, admin functions.

## Risks & Mitigation

| Risk                       | Mitigation                          |
|----------------------------|-------------------------------------|
| Code bugs                  | Manual and code review testing      |
| Score file corruption      | File handling with error checking   |
| User confusion             | Clear instructions, feedback        |
| Platform issues            | Use Python and Pygame (cross-platform)|
| Admin password leaks       | Allow easy password change in code  |
