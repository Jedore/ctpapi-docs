<table border="0" cellspacing="0" class="square-block" id=""><tbody border="0"><tr border="0"><td class="square-block-left"></td><td class="square-block-content"><div>

</div></td><td class="square-block-right"></td></tr></tbody></table>
<p>CthostFtdcMdApi类提供了行情api的初始化、登录、订阅等功能。</p>
<span class="anchor" id="78e3798f-f7e0-4571-8847-be41badbba10"></span>
## 1.接口
<pre><code>class MD_API_EXPORT CThostFtdcMdApi
{
public:
    ///创建MdApi
    ///@param pszFlowPath 存贮订阅信息文件的目录，默认为当前目录
    ///@return 创建出的UserApi
    ///modify for udp marketdata
    static CThostFtdcMdApi *CreateFtdcMdApi(const char *pszFlowPath = "", const bool bIsUsingUdp=false, const bool bIsMulticast=false);
    ///获取API的版本信息
    ///@retrun 获取到的版本号
    static const char *GetApiVersion();
    ///删除接口对象本身
    ///@remark 不再使用本接口对象时,调用该函数删除接口对象
    virtual void Release() = 0;
    ///初始化
    ///@remark 初始化运行环境,只有调用后,接口才开始工作
    virtual void Init() = 0;
    ///等待接口线程结束运行
    ///@return 线程退出代码
    virtual int Join() = 0;
    ///获取当前交易日
    ///@retrun 获取到的交易日
    ///@remark 只有登录成功后,才能得到正确的交易日
    virtual const char *GetTradingDay() = 0;
    ///注册前置机网络地址
    ///@param pszFrontAddress：前置机网络地址。
    ///@remark 网络地址的格式为：“protocol://ipaddress:port”，如：”tcp://127.0.0.1:17001”。 
    ///@remark “tcp”代表传输协议，“127.0.0.1”代表服务器地址。”17001”代表服务器端口号。
    virtual void RegisterFront(char *pszFrontAddress) = 0;
    ///注册名字服务器网络地址
    ///@param pszNsAddress：名字服务器网络地址。
    ///@remark 网络地址的格式为：“protocol://ipaddress:port”，如：”tcp://127.0.0.1:12001”。 
    ///@remark “tcp”代表传输协议，“127.0.0.1”代表服务器地址。”12001”代表服务器端口号。
    ///@remark RegisterNameServer优先于RegisterFront
    virtual void RegisterNameServer(char *pszNsAddress) = 0;
    ///注册名字服务器用户信息
    ///@param pFensUserInfo：用户信息。
    virtual void RegisterFensUserInfo(CThostFtdcFensUserInfoField * pFensUserInfo) = 0;
    ///注册回调接口
    ///@param pSpi 派生自回调接口类的实例
    virtual void RegisterSpi(CThostFtdcMdSpi *pSpi) = 0;
    ///订阅行情。
    ///@param ppInstrumentID 合约ID  
    ///@param nCount 要订阅/退订行情的合约个数
    ///@remark 
    virtual int SubscribeMarketData(char *ppInstrumentID[], int nCount) = 0;
    ///退订行情。
    ///@param ppInstrumentID 合约ID  
    ///@param nCount 要订阅/退订行情的合约个数
    ///@remark 
    virtual int UnSubscribeMarketData(char *ppInstrumentID[], int nCount) = 0;
    ///订阅询价。
    ///@param ppInstrumentID 合约ID  
    ///@param nCount 要订阅/退订行情的合约个数
    ///@remark 
    virtual int SubscribeForQuoteRsp(char *ppInstrumentID[], int nCount) = 0;
    ///退订询价。
    ///@param ppInstrumentID 合约ID  
    ///@param nCount 要订阅/退订行情的合约个数
    ///@remark 
    virtual int UnSubscribeForQuoteRsp(char *ppInstrumentID[], int nCount) = 0;
    ///用户登录请求
    virtual int ReqUserLogin(CThostFtdcReqUserLoginField *pReqUserLoginField, int nRequestID) = 0;
    ///登出请求
    virtual int ReqUserLogout(CThostFtdcUserLogoutField *pUserLogout, int nRequestID) = 0;
    ///请求查询组播合约
    virtual int ReqQryMulticastInstrument(CThostFtdcQryMulticastInstrumentField *pQryMulticastInstrument, int nRequestID) = 0;
protected:
    ~CThostFtdcMdApi(){};
};
</code></pre>
<span class="anchor" id="d6724d7a-67f5-47e3-ae73-843a17921642"></span>
## 2.示例代码
<pre><code>class CMduserHandler : public CThostFtdcMdSpi
{
private:
    CThostFtdcMdApi *m_mdApi;
public:
    void connect()
    {
        //创建并初始化API，按照以下顺序
        m_mdApi = CThostFtdcMdApi::CreateFtdcMdApi("", true, true);
        m_mdApi-&gt;RegisterSpi(this);
        m_mdApi-&gt;RegisterFront("tcp://127.0.0.1:41413");
        m_mdApi-&gt;Init();
    }
}
</code></pre>
<div class="sub-links-list" style="text-indent:0px;"><hr class="SubLinksListLine"/>
<p class="sub-links-list-header">请参阅：</p>
<p class="sub-links-paragraph">    <a class="sub-links-action" href="../CREATEFTDCMDAPI/">CreateFtdcMdApi</a></p>
<p class="sub-links-paragraph">    <a class="sub-links-action" href="../GETAPIVERSION/">GetApiVersion</a></p>
<p class="sub-links-paragraph">    <a class="sub-links-action" href="../GETTRADINGDAY/">GetTradingDay</a></p>
<p class="sub-links-paragraph">    <a class="sub-links-action" href="../INIT/">Init</a></p>
<p class="sub-links-paragraph">    <a class="sub-links-action" href="../JOIN/">Join</a></p>
<p class="sub-links-paragraph">    <a class="sub-links-action" href="../REGISTERFENSUSERINFO/">RegisterFensUserInfo</a></p>
<p class="sub-links-paragraph">    <a class="sub-links-action" href="../REGISTERFRONT/">RegisterFront</a></p>
<p class="sub-links-paragraph">    <a class="sub-links-action" href="../REGISTERNAMESERVER/">RegisterNameServer</a></p>
<p class="sub-links-paragraph">    <a class="sub-links-action" href="../REGISTERSPI/">RegisterSpi</a></p>
<p class="sub-links-paragraph">    <a class="sub-links-action" href="../RELEASE/">Release</a></p>
<p class="sub-links-paragraph">    <a class="sub-links-action" href="../REQQRYMULTICASTINSTRUMENT/">ReqQryMulticastInstrument</a></p>
<p class="sub-links-paragraph">    <a class="sub-links-action" href="../REQUSERLOGIN/">ReqUserLogin</a></p>
<p class="sub-links-paragraph">    <a class="sub-links-action" href="../REQUSERLOGOUT/">ReqUserLogout</a></p>
<p class="sub-links-paragraph">    <a class="sub-links-action" href="../SUBSCRIBEFORQUOTERSP/">SubscribeForQuoteRsp</a></p>
<p class="sub-links-paragraph">    <a class="sub-links-action" href="../SUBSCRIBEMARKETDATA/">SubscribeMarketData</a></p>
<p class="sub-links-paragraph">    <a class="sub-links-action" href="../UNSUBSCRIBEFORQUOTERSP/">UnSubscribeForQuoteRsp</a></p>
<p class="sub-links-paragraph">    <a class="sub-links-action" href="../UNSUBSCRIBEMARKETDATA/">UnSubscribeMarketData</a></p>
</div>
