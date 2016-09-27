/*
 * Copyright (C) 2015 Glyptodon LLC
 *
 * Permission is hereby granted, free of charge, to any person obtaining a copy
 * of this software and associated documentation files (the "Software"), to deal
 * in the Software without restriction, including without limitation the rights
 * to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 * copies of the Software, and to permit persons to whom the Software is
 * furnished to do so, subject to the following conditions:
 *
 * The above copyright notice and this permission notice shall be included in
 * all copies or substantial portions of the Software.
 *
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 * IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 * FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 * AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 * LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 * OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
 * THE SOFTWARE.
 */

package org.glyptodon.guacamole.auth.jdbc.permission;

import org.glyptodon.guacamole.auth.jdbc.user.ModeledUser;
import com.google.inject.Inject;
import java.util.Collections;
import java.util.Set;
import org.glyptodon.guacamole.auth.jdbc.user.AuthenticatedUser;
import org.glyptodon.guacamole.GuacamoleException;
import org.glyptodon.guacamole.auth.jdbc.base.RestrictedObject;
import org.glyptodon.guacamole.net.auth.permission.SystemPermission;

/**
 * A database implementation of SystemPermissionSet which uses an injected
 * service to query and manipulate the system permissions associated with a
 * particular user.
 *
 * @author Michael Jumper
 */
public class SystemPermissionSet extends RestrictedObject
    implements org.glyptodon.guacamole.net.auth.permission.SystemPermissionSet {

    /**
     * The user associated with this permission set. Each of the permissions in
     * this permission set is granted to this user.
     */
    private ModeledUser user;

    /**
     * Service for reading and manipulating system permissions.
     */
    @Inject
    private SystemPermissionService systemPermissionService;
    
    /**
     * Creates a new SystemPermissionSet. The resulting permission set
     * must still be initialized by a call to init(), or the information
     * necessary to read and modify this set will be missing.
     */
    public SystemPermissionSet() {
    }

    /**
     * Initializes this permission set with the current user and the user
     * to whom the permissions in this set are granted.
     *
     * @param currentUser
     *     The user who queried this permission set, and whose permissions
     *     dictate the access level of all operations performed on this set.
     *
     * @param user
     *     The user to whom the permissions in this set are granted.
     */
    public void init(AuthenticatedUser currentUser, ModeledUser user) {
        super.init(currentUser);
        this.user = user;
    }

    @Override
    public Set<SystemPermission> getPermissions() throws GuacamoleException {
        return systemPermissionService.retrievePermissions(getCurrentUser(), user);
    }

    @Override
    public boolean hasPermission(SystemPermission.Type permission)
            throws GuacamoleException {
        return systemPermissionService.retrievePermission(getCurrentUser(), user, permission) != null;
    }

    @Override
    public void addPermission(SystemPermission.Type permission)
            throws GuacamoleException {
        addPermissions(Collections.singleton(new SystemPermission(permission)));
    }

    @Override
    public void removePermission(SystemPermission.Type permission)
            throws GuacamoleException {
        removePermissions(Collections.singleton(new SystemPermission(permission)));
    }

    @Override
    public void addPermissions(Set<SystemPermission> permissions)
            throws GuacamoleException {
        systemPermissionService.createPermissions(getCurrentUser(), user, permissions);
    }

    @Override
    public void removePermissions(Set<SystemPermission> permissions)
            throws GuacamoleException {
        systemPermissionService.deletePermissions(getCurrentUser(), user, permissions);
    }

}
