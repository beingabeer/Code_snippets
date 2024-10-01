# Restore Deleted Container Images from JFrog Artifactory Trash

This Python script allows the restoration of container images that have been deleted from JFrog Artifactory's trash can. The restoration is based on the user who deleted the images and a specific time frame.

## Prerequisites

- Python 3.x
- JFrog Artifactory credentials with permissions to query the trash can and restore images.
- The script expects JFrog AQL (Artifactory Query Language) to locate the images in the trash.

## How to Use

### Command Format

To run the script, use the following command format:

```bash
python3 restore.py <USER_ID>

Parameters

    <USER_ID>: The ID of the user whose deleted container images you want to restore.

For example, if the user ID is AIT_NO, the command would look like:

bash

python3 restore.py AIT_NO

What the Script Does

    It searches for container images in the Artifactory trash can that were deleted by the specified user (<USER_ID>).
    It uses JFrog AQL (Artifactory Query Language) to query for the images that were deleted within a particular time frame.
    Once identified, the script copies the images from the trash can back to their original location in the repository.

AQL Explanation

The script uses JFrog's Artifactory Query Language (AQL) to find the deleted images in the trash. AQL allows querying of Artifactory repositories with great precision. Here’s a typical AQL query for this scenario:

aql

items.find({
    "repo": "trash-can-repo",
    "name": {"$match": "*.tar"},
    "deleted": {"$eq": true},
    "deleted_by": {"$eq": "<USER_ID>"},
    "deleted_date": {
        "$gt": "<START_DATE>",
        "$lt": "<END_DATE>"
    }
})

Breakdown of the AQL:

    "repo": "trash-can-repo": This specifies the repository where deleted items are stored (trash can).
    "name": {"$match": "*.tar"}: This matches files with the extension .tar, which typically represent container images.
    "deleted": {"$eq": true}: Filters only the deleted items.
    "deleted_by": {"$eq": "<USER_ID>"}: Limits the search to items deleted by a specific user.
    "deleted_date": { "$gt": "<START_DATE>", "$lt": "<END_DATE>" }: Filters items deleted within a certain time frame.

Replace <USER_ID>, <START_DATE>, and <END_DATE> with the appropriate values when running the query.
Error Handling

In case of errors such as invalid user ID or no images found within the specified time frame, the script will log appropriate error messages.
License

This project is licensed under the MIT License.

csharp


You can now copy and paste this version directly into your README.
