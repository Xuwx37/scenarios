# Merge Changes from the New Branch into the Main Branch

The `merge` command is used to combine changes from one branch into another.

## Target

Your goal is to merge changes from the new branch back into the main branch using the `merge` command.

## Result Example

Here's an example of what you should be able to accomplish by the end of this step:

1. Merge changes from the new branch back into the main branch using the merge command.

Make sure you are on the main branch using the checkout command:

```shell
git checkout main
```

Use the following command to merge the changes from the new-branch branch into the main branch:

```shell
git merge new-branch
```

If there are any conflicts during the merge, you will need to resolve them by editing the affected files and using the `git add` command to stage the changes.

Once the merge is complete, use the `git status` command to ensure that the merge was successful.

Use the following command to commit the merge:

```shell
git commit -m "Merge changes from new-branch"
```

This will create a new commit in the main branch that includes the changes from the new-branch branch.

## Requirements

To complete this step, you will need:

- A Git repository with at least one commit.
- A new branch created using the branch command.
- Changes made to a file in the new branch.
- The ability to switch between branches using the checkout command.
