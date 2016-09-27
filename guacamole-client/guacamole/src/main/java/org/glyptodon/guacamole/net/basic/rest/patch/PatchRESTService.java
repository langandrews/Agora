/*
 * Copyright (C) 2016 Glyptodon LLC
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

package org.glyptodon.guacamole.net.basic.rest.patch;

import com.google.inject.Inject;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.Reader;
import java.util.ArrayList;
import java.util.List;
import javax.ws.rs.GET;
import javax.ws.rs.Path;
import javax.ws.rs.Produces;
import javax.ws.rs.core.MediaType;
import org.glyptodon.guacamole.GuacamoleException;
import org.glyptodon.guacamole.GuacamoleServerException;
import org.glyptodon.guacamole.net.basic.extension.PatchResourceService;
import org.glyptodon.guacamole.net.basic.resource.Resource;

/**
 * A REST Service for handling the listing of HTML patches.
 *
 * @author Michael Jumper
 */
@Path("/patches")
@Produces(MediaType.APPLICATION_JSON)
public class PatchRESTService {

    /**
     * Service for retrieving information regarding available HTML patch
     * resources.
     */
    @Inject
    private PatchResourceService patchResourceService;

    /**
     * Reads the entire contents of the given resource as a String. The
     * resource is assumed to be encoded in UTF-8.
     *
     * @param resource
     *     The resource to read as a new String.
     *
     * @return
     *     A new String containing the contents of the given resource.
     *
     * @throws IOException
     *     If an I/O error prevents reading the resource.
     */
    private String readResourceAsString(Resource resource) throws IOException {

        StringBuilder contents = new StringBuilder();

        // Read entire resource into StringBuilder one chunk at a time
        Reader reader = new InputStreamReader(resource.asStream(), "UTF-8");
        try {

            char buffer[] = new char[8192];
            int length;

            while ((length = reader.read(buffer)) != -1) {
                contents.append(buffer, 0, length);
            }

        }

        // Ensure resource is always closed
        finally {
            reader.close();
        }

        return contents.toString();

    }

    /**
     * Returns a list of all available HTML patches, in the order they should
     * be applied. Each patch is raw HTML containing additional meta tags
     * describing how and where the patch should be applied.
     *
     * @return
     *     A list of all HTML patches defined in the system, in the order they
     *     should be applied.
     *
     * @throws GuacamoleException
     *     If an error occurs preventing any HTML patch from being read.
     */
    @GET
    public List<String> getPatches() throws GuacamoleException {

        try {

            // Allocate a list of equal size to the total number of patches
            List<Resource> resources = patchResourceService.getPatchResources();
            List<String> patches = new ArrayList<String>(resources.size());

            // Convert each patch resource to a string
            for (Resource resource : resources) {
                patches.add(readResourceAsString(resource));
            }

            // Return all patches in string form
            return patches;

        }

        // Bail out entirely on error
        catch (IOException e) {
            throw new GuacamoleServerException("Unable to read HTML patches.", e);
        }

    }

}
