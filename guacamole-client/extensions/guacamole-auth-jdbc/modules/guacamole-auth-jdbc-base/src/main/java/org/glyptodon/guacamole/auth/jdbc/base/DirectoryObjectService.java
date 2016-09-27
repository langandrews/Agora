/*
 * Copyright (C) 2013 Glyptodon LLC
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

package org.glyptodon.guacamole.auth.jdbc.base;

import java.util.Collection;
import java.util.Set;
import org.glyptodon.guacamole.auth.jdbc.user.AuthenticatedUser;
import org.glyptodon.guacamole.GuacamoleException;

/**
 * Service which provides convenience methods for creating, retrieving, and
 * manipulating objects that have unique identifiers, such as the objects
 * within directories. This service will automatically enforce the permissions
 * of the current user.
 *
 * @author Michael Jumper
 * @param <InternalType>
 *     The specific internal implementation of the type of object this service
 *     provides access to.
 *
 * @param <ExternalType>
 *     The external interface or implementation of the type of object this
 *     service provides access to, as defined by the guacamole-ext API.
 */
public interface DirectoryObjectService<InternalType, ExternalType> {

    /**
     * Retrieves the single object that has the given identifier, if it exists
     * and the user has permission to read it.
     *
     * @param user
     *     The user retrieving the object.
     *
     * @param identifier
     *     The identifier of the object to retrieve.
     *
     * @return
     *     The object having the given identifier, or null if no such object
     *     exists.
     *
     * @throws GuacamoleException
     *     If an error occurs while retrieving the requested object.
     */
    InternalType retrieveObject(AuthenticatedUser user, String identifier)
            throws GuacamoleException;
    
    /**
     * Retrieves all objects that have the identifiers in the given collection.
     * Only objects that the user has permission to read will be returned.
     *
     * @param user
     *     The user retrieving the objects.
     *
     * @param identifiers
     *     The identifiers of the objects to retrieve.
     *
     * @return
     *     The objects having the given identifiers.
     *
     * @throws GuacamoleException
     *     If an error occurs while retrieving the requested objects.
     */
    Collection<InternalType> retrieveObjects(AuthenticatedUser user,
            Collection<String> identifiers) throws GuacamoleException;

    /**
     * Creates the given object. If the object already exists, an error will be
     * thrown.
     *
     * @param user
     *     The user creating the object.
     *
     * @param object
     *     The object to create.
     *
     * @return
     *     The newly-created object.
     *
     * @throws GuacamoleException
     *     If the user lacks permission to create the object, or an error
     *     occurs while creating the object.
     */
    InternalType createObject(AuthenticatedUser user, ExternalType object)
            throws GuacamoleException;

    /**
     * Deletes the object having the given identifier. If no such object
     * exists, this function has no effect.
     *
     * @param user
     *     The user deleting the object.
     *
     * @param identifier
     *     The identifier of the object to delete.
     *
     * @throws GuacamoleException
     *     If the user lacks permission to delete the object, or an error
     *     occurs while deleting the object.
     */
    void deleteObject(AuthenticatedUser user, String identifier)
        throws GuacamoleException;

    /**
     * Updates the given object, applying any changes that have been made. If
     * no such object exists, this function has no effect.
     *
     * @param user
     *     The user updating the object.
     *
     * @param object
     *     The object to update.
     *
     * @throws GuacamoleException
     *     If the user lacks permission to update the object, or an error
     *     occurs while updating the object.
     */
    void updateObject(AuthenticatedUser user, InternalType object)
            throws GuacamoleException;

    /**
     * Returns the set of all identifiers for all objects that the user has
     * read access to.
     *
     * @param user
     *     The user retrieving the identifiers.
     *
     * @return
     *     The set of all identifiers for all objects.
     *
     * @throws GuacamoleException
     *     If an error occurs while reading identifiers.
     */
    Set<String> getIdentifiers(AuthenticatedUser user) throws GuacamoleException;

}
