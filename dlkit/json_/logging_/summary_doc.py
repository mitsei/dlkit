# -*- coding: utf-8 -*-
"""Logging Open Service Interface Definitions
logging version 3.0.0

The Logging OSID provides a means to read and wite to logs. A Log
represents a collection of log entries. Each log entry is composed of a
priority ``Type,`` timestamp, ``Agent,`` the agent's associated
``Resource,`` and a record.

Logs can be organized into hierarchies for federation. A log that is a
parent of another log makes visible the log entries of its children.

Example
  LoggingSession out = manager.getLoggingSession();
  out.log(warningLogEntryPriorityType, "hello world", stringLogEntryContentType);

  LogReadingSession in = manager.getLogReadingSession();
  LogEntryList entries = inn.getLogEntries();
  while (entries.hasNext()) {
      LogEntry entry = entries.getNextLogEntry();
      printEntry(entry);
  }

"""
