/*
 * Licensed to the Apache Software Foundation (ASF) under one
 * or more contributor license agreements.  See the NOTICE file
 * distributed with this work for additional information
 * regarding copyright ownership.  The ASF licenses this file
 * to you under the Apache License, Version 2.0 (the
 * "License"); you may not use this file except in compliance
 * with the License.  You may obtain a copy of the License at
 *
 *   http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing,
 * software distributed under the License is distributed on an
 * "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
 * KIND, either express or implied.  See the License for the
 * specific language governing permissions and limitations
 * under the License.
 */

package com.epam.datalab.backendapi.domain;

import com.fasterxml.jackson.annotation.JsonProperty;
import lombok.Data;

import javax.validation.constraints.NotNull;
import javax.validation.constraints.Pattern;
import java.util.Set;

@Data
public class CreateProjectDTO {
    @NotNull
    private final String name;
    @NotNull
    private final Set<String> groups;
    @NotNull
    final Set<String> endpoints;
    @NotNull
    @Pattern(regexp = "^ssh-.*\\n?", message = "format is incorrect. Please use the openSSH format")
    private final String key;
    @NotNull
    private final String tag;
    @JsonProperty("shared_image_enabled")
    private boolean sharedImageEnabled;
}