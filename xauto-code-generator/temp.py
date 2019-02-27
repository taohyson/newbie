'''
@Component
public class ''' + className + ''' extends SimpleChannelInboundHandler<Object> {
    private static Logger logger = LogManager.getLogger();
    
    private String ''' + uriPrefix + ''';

    public static ''' + dict["type"] + ''' get''' + dict["name"].capitalize() + '''{
        String ret = "";
        ret += ''' + dict["description"] + ''';
        return ret;
    }

    ''' + expand(array, lambda item:'''
    public static ''' + item["type"] + ''' get''' + item["name"].capitalize() + '''{
        String ret = "";
        return ret;
    }
    
    ''') + '''
}
'''