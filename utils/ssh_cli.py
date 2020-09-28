#!/usr/bin/env python3

__author__ = "Catalin Dinuta"


class SSHCli:
    """File downloader and uploader similar with transferring files over SSH"""
    actions = ["--download", "--upload"]

    @staticmethod
    def upload_file(service, remote_path, local_path):
        return service.upload_file(remote_path=remote_path, local_path=local_path)

    @staticmethod
    def download_file(service, remote_path, local_path):
        return service.download_file(remote_path=remote_path, local_path=local_path)

    @staticmethod
    def check_action(action):
        if action not in SSHCli.actions:
            raise Exception(f"Invalid action: {action}. Valid actions are: {SSHCli.actions}")
