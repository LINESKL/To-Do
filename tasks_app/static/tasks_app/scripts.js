
document.addEventListener("DOMContentLoaded", function () {
    const sidebarToggleBtn = document.querySelector("#sidebarToggle");
    const sidebar = document.querySelector(".sidebar");
    const content = document.querySelector(".content");

    // Menu toggle functionality
    if (sidebarToggleBtn) {
        sidebarToggleBtn.addEventListener("click", function () {
            sidebar.classList.toggle("hidden");
            content.classList.toggle("expanded");
        });
    }

    // Ensure that the form is submitted properly
    const taskForm = document.querySelector(".task-form");
    if (taskForm) {
        taskForm.addEventListener("submit", function (event) {
            event.preventDefault();  // Prevent default submission behavior
            taskForm.submit();  // Explicitly submit the form
        });
    }
});
