<table border="0" cellspacing="0" class="square-block" id=""><tbody border="0"><tr border="0"><td class="square-block-left"></td><td class="square-block-content"><div>

</div></td><td class="square-block-right"></td></tr></tbody></table>
<p>CThostFtdcTraderApi类提供了交易api的初始化、登录、报单和查询等功能。</p>
<span class="anchor" id="ea49b423-39b6-4c49-b9b1-cbf524b3b40c"></span>
## 1.接口
<pre><code>class TRADER_API_EXPORT CThostFtdcTraderApi
{
public:
    ///创建TraderApi
    ///@param pszFlowPath 存贮订阅信息文件的目录，默认为当前目录
    ///@return 创建出的UserApi
    static CThostFtdcTraderApi *CreateFtdcTraderApi(const char *pszFlowPath = "");
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
    virtual void RegisterSpi(CThostFtdcTraderSpi *pSpi) = 0;
    ///订阅私有流。
    ///@param nResumeType 私有流重传方式  
    ///        THOST_TERT_RESTART:从本交易日开始重传
    ///        THOST_TERT_RESUME:从上次收到的续传
    ///        THOST_TERT_QUICK:只传送登录后私有流的内容
    ///@remark 该方法要在Init方法前调用。若不调用则不会收到私有流的数据。
    virtual void SubscribePrivateTopic(THOST_TE_RESUME_TYPE nResumeType) = 0;
    ///订阅公共流。
    ///@param nResumeType 公共流重传方式  
    ///        THOST_TERT_RESTART:从本交易日开始重传
    ///        THOST_TERT_RESUME:从上次收到的续传
    ///        THOST_TERT_QUICK:只传送登录后公共流的内容
    ///@remark 该方法要在Init方法前调用。若不调用则不会收到公共流的数据。
    virtual void SubscribePublicTopic(THOST_TE_RESUME_TYPE nResumeType) = 0;
    ///客户端认证请求
    virtual int ReqAuthenticate(CThostFtdcReqAuthenticateField *pReqAuthenticateField, int nRequestID) = 0;
    ///注册用户终端信息，用于中继服务器多连接模式
    ///需要在终端认证成功后，用户登录前调用该接口
    virtual int RegisterUserSystemInfo(CThostFtdcUserSystemInfoField *pUserSystemInfo) = 0;
    ///上报用户终端信息，用于中继服务器操作员登录模式
    ///操作员登录后，可以多次调用该接口上报客户信息
    virtual int SubmitUserSystemInfo(CThostFtdcUserSystemInfoField *pUserSystemInfo) = 0;
    ///用户登录请求
    virtual int ReqUserLogin(CThostFtdcReqUserLoginField *pReqUserLoginField, int nRequestID) = 0;
    ///登出请求
    virtual int ReqUserLogout(CThostFtdcUserLogoutField *pUserLogout, int nRequestID) = 0;
    ///用户口令更新请求
    virtual int ReqUserPasswordUpdate(CThostFtdcUserPasswordUpdateField *pUserPasswordUpdate, int nRequestID) = 0;
    ///资金账户口令更新请求
    virtual int ReqTradingAccountPasswordUpdate(CThostFtdcTradingAccountPasswordUpdateField *pTradingAccountPasswordUpdate, int nRequestID) = 0;
    ///查询用户当前支持的认证模式
    virtual int ReqUserAuthMethod(CThostFtdcReqUserAuthMethodField *pReqUserAuthMethod, int nRequestID) = 0;
    ///用户发出获取图形验证码请求
    virtual int ReqGenUserCaptcha(CThostFtdcReqGenUserCaptchaField *pReqGenUserCaptcha, int nRequestID) = 0;
    ///用户发出获取短信验证码请求
    virtual int ReqGenUserText(CThostFtdcReqGenUserTextField *pReqGenUserText, int nRequestID) = 0;
    ///用户发出带有图片验证码的登陆请求
    virtual int ReqUserLoginWithCaptcha(CThostFtdcReqUserLoginWithCaptchaField *pReqUserLoginWithCaptcha, int nRequestID) = 0;
    ///用户发出带有短信验证码的登陆请求
    virtual int ReqUserLoginWithText(CThostFtdcReqUserLoginWithTextField *pReqUserLoginWithText, int nRequestID) = 0;
    ///用户发出带有动态口令的登陆请求
    virtual int ReqUserLoginWithOTP(CThostFtdcReqUserLoginWithOTPField *pReqUserLoginWithOTP, int nRequestID) = 0;
    ///报单录入请求
    virtual int ReqOrderInsert(CThostFtdcInputOrderField *pInputOrder, int nRequestID) = 0;
    ///预埋单录入请求
    virtual int ReqParkedOrderInsert(CThostFtdcParkedOrderField *pParkedOrder, int nRequestID) = 0;
    ///预埋撤单录入请求
    virtual int ReqParkedOrderAction(CThostFtdcParkedOrderActionField *pParkedOrderAction, int nRequestID) = 0;
    ///报单操作请求
    virtual int ReqOrderAction(CThostFtdcInputOrderActionField *pInputOrderAction, int nRequestID) = 0;
    ///查询最大报单数量请求
    virtual int ReqQueryMaxOrderVolume(CThostFtdcQueryMaxOrderVolumeField *pQueryMaxOrderVolume, int nRequestID) = 0;
    ///投资者结算结果确认
    virtual int ReqSettlementInfoConfirm(CThostFtdcSettlementInfoConfirmField *pSettlementInfoConfirm, int nRequestID) = 0;
    ///请求删除预埋单
    virtual int ReqRemoveParkedOrder(CThostFtdcRemoveParkedOrderField *pRemoveParkedOrder, int nRequestID) = 0;
    ///请求删除预埋撤单
    virtual int ReqRemoveParkedOrderAction(CThostFtdcRemoveParkedOrderActionField *pRemoveParkedOrderAction, int nRequestID) = 0;
    ///执行宣告录入请求
    virtual int ReqExecOrderInsert(CThostFtdcInputExecOrderField *pInputExecOrder, int nRequestID) = 0;
    ///执行宣告操作请求
    virtual int ReqExecOrderAction(CThostFtdcInputExecOrderActionField *pInputExecOrderAction, int nRequestID) = 0;
    ///询价录入请求
    virtual int ReqForQuoteInsert(CThostFtdcInputForQuoteField *pInputForQuote, int nRequestID) = 0;
    ///报价录入请求
    virtual int ReqQuoteInsert(CThostFtdcInputQuoteField *pInputQuote, int nRequestID) = 0;
    ///报价操作请求
    virtual int ReqQuoteAction(CThostFtdcInputQuoteActionField *pInputQuoteAction, int nRequestID) = 0;
    ///批量报单操作请求
    virtual int ReqBatchOrderAction(CThostFtdcInputBatchOrderActionField *pInputBatchOrderAction, int nRequestID) = 0;
    ///期权自对冲录入请求
    virtual int ReqOptionSelfCloseInsert(CThostFtdcInputOptionSelfCloseField *pInputOptionSelfClose, int nRequestID) = 0;
    ///期权自对冲操作请求
    virtual int ReqOptionSelfCloseAction(CThostFtdcInputOptionSelfCloseActionField *pInputOptionSelfCloseAction, int nRequestID) = 0;
    ///申请组合录入请求
    virtual int ReqCombActionInsert(CThostFtdcInputCombActionField *pInputCombAction, int nRequestID) = 0;
    ///请求查询报单
    virtual int ReqQryOrder(CThostFtdcQryOrderField *pQryOrder, int nRequestID) = 0;
    ///请求查询成交
    virtual int ReqQryTrade(CThostFtdcQryTradeField *pQryTrade, int nRequestID) = 0;
    ///请求查询投资者持仓
    virtual int ReqQryInvestorPosition(CThostFtdcQryInvestorPositionField *pQryInvestorPosition, int nRequestID) = 0;
    ///请求查询资金账户
    virtual int ReqQryTradingAccount(CThostFtdcQryTradingAccountField *pQryTradingAccount, int nRequestID) = 0;
    ///请求查询投资者
    virtual int ReqQryInvestor(CThostFtdcQryInvestorField *pQryInvestor, int nRequestID) = 0;
    ///请求查询交易编码
    virtual int ReqQryTradingCode(CThostFtdcQryTradingCodeField *pQryTradingCode, int nRequestID) = 0;
    ///请求查询合约保证金率
    virtual int ReqQryInstrumentMarginRate(CThostFtdcQryInstrumentMarginRateField *pQryInstrumentMarginRate, int nRequestID) = 0;
    ///请求查询合约手续费率
    virtual int ReqQryInstrumentCommissionRate(CThostFtdcQryInstrumentCommissionRateField *pQryInstrumentCommissionRate, int nRequestID) = 0;
    ///请求查询交易所
    virtual int ReqQryExchange(CThostFtdcQryExchangeField *pQryExchange, int nRequestID) = 0;
    ///请求查询产品
    virtual int ReqQryProduct(CThostFtdcQryProductField *pQryProduct, int nRequestID) = 0;
    ///请求查询合约
    virtual int ReqQryInstrument(CThostFtdcQryInstrumentField *pQryInstrument, int nRequestID) = 0;
    ///请求查询行情
    virtual int ReqQryDepthMarketData(CThostFtdcQryDepthMarketDataField *pQryDepthMarketData, int nRequestID) = 0;
    ///请求查询投资者结算结果
    virtual int ReqQrySettlementInfo(CThostFtdcQrySettlementInfoField *pQrySettlementInfo, int nRequestID) = 0;
    ///请求查询转帐银行
    virtual int ReqQryTransferBank(CThostFtdcQryTransferBankField *pQryTransferBank, int nRequestID) = 0;
    ///请求查询投资者持仓明细
    virtual int ReqQryInvestorPositionDetail(CThostFtdcQryInvestorPositionDetailField *pQryInvestorPositionDetail, int nRequestID) = 0;
    ///请求查询客户通知
    virtual int ReqQryNotice(CThostFtdcQryNoticeField *pQryNotice, int nRequestID) = 0;
    ///请求查询结算信息确认
    virtual int ReqQrySettlementInfoConfirm(CThostFtdcQrySettlementInfoConfirmField *pQrySettlementInfoConfirm, int nRequestID) = 0;
    ///请求查询投资者持仓明细
    virtual int ReqQryInvestorPositionCombineDetail(CThostFtdcQryInvestorPositionCombineDetailField *pQryInvestorPositionCombineDetail, int nRequestID) = 0;
    ///请求查询保证金监管系统经纪公司资金账户密钥
    virtual int ReqQryCFMMCTradingAccountKey(CThostFtdcQryCFMMCTradingAccountKeyField *pQryCFMMCTradingAccountKey, int nRequestID) = 0;
    ///请求查询仓单折抵信息
    virtual int ReqQryEWarrantOffset(CThostFtdcQryEWarrantOffsetField *pQryEWarrantOffset, int nRequestID) = 0;
    ///请求查询投资者品种/跨品种保证金
    virtual int ReqQryInvestorProductGroupMargin(CThostFtdcQryInvestorProductGroupMarginField *pQryInvestorProductGroupMargin, int nRequestID) = 0;
    ///请求查询交易所保证金率
    virtual int ReqQryExchangeMarginRate(CThostFtdcQryExchangeMarginRateField *pQryExchangeMarginRate, int nRequestID) = 0;
    ///请求查询交易所调整保证金率
    virtual int ReqQryExchangeMarginRateAdjust(CThostFtdcQryExchangeMarginRateAdjustField *pQryExchangeMarginRateAdjust, int nRequestID) = 0;
    ///请求查询汇率
    virtual int ReqQryExchangeRate(CThostFtdcQryExchangeRateField *pQryExchangeRate, int nRequestID) = 0;
    ///请求查询二级代理操作员银期权限
    virtual int ReqQrySecAgentACIDMap(CThostFtdcQrySecAgentACIDMapField *pQrySecAgentACIDMap, int nRequestID) = 0;
    ///请求查询产品报价汇率
    virtual int ReqQryProductExchRate(CThostFtdcQryProductExchRateField *pQryProductExchRate, int nRequestID) = 0;
    ///请求查询产品组
    virtual int ReqQryProductGroup(CThostFtdcQryProductGroupField *pQryProductGroup, int nRequestID) = 0;
    ///请求查询做市商合约手续费率
    virtual int ReqQryMMInstrumentCommissionRate(CThostFtdcQryMMInstrumentCommissionRateField *pQryMMInstrumentCommissionRate, int nRequestID) = 0;
    ///请求查询做市商期权合约手续费
    virtual int ReqQryMMOptionInstrCommRate(CThostFtdcQryMMOptionInstrCommRateField *pQryMMOptionInstrCommRate, int nRequestID) = 0;
    ///请求查询报单手续费
    virtual int ReqQryInstrumentOrderCommRate(CThostFtdcQryInstrumentOrderCommRateField *pQryInstrumentOrderCommRate, int nRequestID) = 0;
    ///请求查询资金账户
    virtual int ReqQrySecAgentTradingAccount(CThostFtdcQryTradingAccountField *pQryTradingAccount, int nRequestID) = 0;
    ///请求查询二级代理商资金校验模式
    virtual int ReqQrySecAgentCheckMode(CThostFtdcQrySecAgentCheckModeField *pQrySecAgentCheckMode, int nRequestID) = 0;
    ///请求查询二级代理商信息
    virtual int ReqQrySecAgentTradeInfo(CThostFtdcQrySecAgentTradeInfoField *pQrySecAgentTradeInfo, int nRequestID) = 0;
    ///请求查询期权交易成本
    virtual int ReqQryOptionInstrTradeCost(CThostFtdcQryOptionInstrTradeCostField *pQryOptionInstrTradeCost, int nRequestID) = 0;
    ///请求查询期权合约手续费
    virtual int ReqQryOptionInstrCommRate(CThostFtdcQryOptionInstrCommRateField *pQryOptionInstrCommRate, int nRequestID) = 0;
    ///请求查询执行宣告
    virtual int ReqQryExecOrder(CThostFtdcQryExecOrderField *pQryExecOrder, int nRequestID) = 0;
    ///请求查询询价
    virtual int ReqQryForQuote(CThostFtdcQryForQuoteField *pQryForQuote, int nRequestID) = 0;
    ///请求查询报价
    virtual int ReqQryQuote(CThostFtdcQryQuoteField *pQryQuote, int nRequestID) = 0;
    ///请求查询期权自对冲
    virtual int ReqQryOptionSelfClose(CThostFtdcQryOptionSelfCloseField *pQryOptionSelfClose, int nRequestID) = 0;
    ///请求查询投资单元
    virtual int ReqQryInvestUnit(CThostFtdcQryInvestUnitField *pQryInvestUnit, int nRequestID) = 0;
    ///请求查询组合合约安全系数
    virtual int ReqQryCombInstrumentGuard(CThostFtdcQryCombInstrumentGuardField *pQryCombInstrumentGuard, int nRequestID) = 0;
    ///请求查询申请组合
    virtual int ReqQryCombAction(CThostFtdcQryCombActionField *pQryCombAction, int nRequestID) = 0;
    ///请求查询转帐流水
    virtual int ReqQryTransferSerial(CThostFtdcQryTransferSerialField *pQryTransferSerial, int nRequestID) = 0;
    ///请求查询银期签约关系
    virtual int ReqQryAccountregister(CThostFtdcQryAccountregisterField *pQryAccountregister, int nRequestID) = 0;
    ///请求查询签约银行
    virtual int ReqQryContractBank(CThostFtdcQryContractBankField *pQryContractBank, int nRequestID) = 0;
    ///请求查询预埋单
    virtual int ReqQryParkedOrder(CThostFtdcQryParkedOrderField *pQryParkedOrder, int nRequestID) = 0;
    ///请求查询预埋撤单
    virtual int ReqQryParkedOrderAction(CThostFtdcQryParkedOrderActionField *pQryParkedOrderAction, int nRequestID) = 0;
    ///请求查询交易通知
    virtual int ReqQryTradingNotice(CThostFtdcQryTradingNoticeField *pQryTradingNotice, int nRequestID) = 0;
    ///请求查询经纪公司交易参数
    virtual int ReqQryBrokerTradingParams(CThostFtdcQryBrokerTradingParamsField *pQryBrokerTradingParams, int nRequestID) = 0;
    ///请求查询经纪公司交易算法
    virtual int ReqQryBrokerTradingAlgos(CThostFtdcQryBrokerTradingAlgosField *pQryBrokerTradingAlgos, int nRequestID) = 0;
    ///请求查询监控中心用户令牌
    virtual int ReqQueryCFMMCTradingAccountToken(CThostFtdcQueryCFMMCTradingAccountTokenField *pQueryCFMMCTradingAccountToken, int nRequestID) = 0;
    ///期货发起银行资金转期货请求
    virtual int ReqFromBankToFutureByFuture(CThostFtdcReqTransferField *pReqTransfer, int nRequestID) = 0;
    ///期货发起期货资金转银行请求
    virtual int ReqFromFutureToBankByFuture(CThostFtdcReqTransferField *pReqTransfer, int nRequestID) = 0;
    ///期货发起查询银行余额请求
    virtual int ReqQueryBankAccountMoneyByFuture(CThostFtdcReqQueryAccountField *pReqQueryAccount, int nRequestID) = 0;
protected:
    ~CThostFtdcTraderApi(){};
};
</code></pre>
<span class="anchor" id="de1c1454-157c-479c-9813-c174afdbb1e4"></span>
## 2.示例代码
<pre><code>class CTraderHandler : public CThostFtdcTraderSpi
{
private:
  CThostFtdcTraderApi *m_ptraderapi;
public:
  void connect()
  {
      //创建API实例，按照以下顺序初始化
      m_ptraderapi = CThostFtdcTraderApi::CreateFtdcTraderApi("flow/"); //必须提前创建好flow目录
      m_ptraderapi-&gt;RegisterSpi(this);
      m_ptraderapi-&gt;SubscribePublicTopic(THOST_TERT_QUICK);
      m_ptraderapi-&gt;SubscribePrivateTopic(THOST_TERT_QUICK); //设置私有流订阅模式
      m_ptraderapi-&gt;RegisterFront("tcp://127.0.0.1:41205");
      m_ptraderapi-&gt;Init();
      //输出API版本信息
      printf("%s\n", m_ptraderapi-&gt;GetApiVersion());
  }
}
</code></pre>
<div class="sub-links-list" style="text-indent:0px;"><hr class="SubLinksListLine"/>
<p class="sub-links-list-header">请参阅：</p>
<p class="sub-links-paragraph">    <a class="sub-links-action" href="../CREATEFTDCTRADERAPI/">CreateFtdcTraderApi</a></p>
<p class="sub-links-paragraph">    <a class="sub-links-action" href="../GETAPIVERSION/">GetApiVersion</a></p>
<p class="sub-links-paragraph">    <a class="sub-links-action" href="../GETTRADINGDAY/">GetTradingDay</a></p>
<p class="sub-links-paragraph">    <a class="sub-links-action" href="../INIT/">Init</a></p>
<p class="sub-links-paragraph">    <a class="sub-links-action" href="../JOIN/">Join</a></p>
<p class="sub-links-paragraph">    <a class="sub-links-action" href="../REGISTERFENSUSERINFO/">RegisterFensUserInfo</a></p>
<p class="sub-links-paragraph">    <a class="sub-links-action" href="../REGISTERFRONT/">RegisterFront</a></p>
<p class="sub-links-paragraph">    <a class="sub-links-action" href="../REGISTERNAMESERVER/">RegisterNameServer</a></p>
<p class="sub-links-paragraph">    <a class="sub-links-action" href="../REGISTERSPI/">RegisterSpi</a></p>
<p class="sub-links-paragraph">    <a class="sub-links-action" href="../REGISTERUSERSYSTEMINFO/">RegisterUserSystemInfo</a></p>
<p class="sub-links-paragraph">    <a class="sub-links-action" href="../RELEASE/">Release</a></p>
<p class="sub-links-paragraph">    <a class="sub-links-action" href="../REQAUTHENTICATE/">ReqAuthenticate</a></p>
<p class="sub-links-paragraph">    <a class="sub-links-action" href="../REQBATCHORDERACTION/">ReqBatchOrderAction</a></p>
<p class="sub-links-paragraph">    <a class="sub-links-action" href="../REQCOMBACTIONINSERT/">ReqCombActionInsert</a></p>
<p class="sub-links-paragraph">    <a class="sub-links-action" href="../REQEXECORDERACTION/">ReqExecOrderAction</a></p>
<p class="sub-links-paragraph">    <a class="sub-links-action" href="../REQEXECORDERINSERT/">ReqExecOrderInsert</a></p>
<p class="sub-links-paragraph">    <a class="sub-links-action" href="../REQFORQUOTEINSERT/">ReqForQuoteInsert</a></p>
<p class="sub-links-paragraph">    <a class="sub-links-action" href="../REQFROMBANKTOFUTUREBYFUTURE/">ReqFromBankToFutureByFuture</a></p>
<p class="sub-links-paragraph">    <a class="sub-links-action" href="../REQFROMFUTURETOBANKBYFUTURE/">ReqFromFutureToBankByFuture</a></p>
<p class="sub-links-paragraph">    <a class="sub-links-action" href="../REQGENUSERCAPTCHA/">ReqGenUserCaptcha</a></p>
<p class="sub-links-paragraph">    <a class="sub-links-action" href="../REQGENUSERTEXT/">ReqGenUserText</a></p>
<p class="sub-links-paragraph">    <a class="sub-links-action" href="../REQOPTIONSELFCLOSEACTION/">ReqOptionSelfCloseAction</a></p>
<p class="sub-links-paragraph">    <a class="sub-links-action" href="../REQOPTIONSELFCLOSEINSERT/">ReqOptionSelfCloseInsert</a></p>
<p class="sub-links-paragraph">    <a class="sub-links-action" href="../REQORDERACTION/">ReqOrderAction</a></p>
<p class="sub-links-paragraph">    <a class="sub-links-action" href="../REQORDERINSERT/">ReqOrderInsert</a></p>
<p class="sub-links-paragraph">    <a class="sub-links-action" href="../REQPARKEDORDERACTION/">ReqParkedOrderAction</a></p>
<p class="sub-links-paragraph">    <a class="sub-links-action" href="../REQPARKEDORDERINSERT/">ReqParkedOrderInsert</a></p>
<p class="sub-links-paragraph">    <a class="sub-links-action" href="../REQQRYACCOUNTREGISTER/">ReqQryAccountregister</a></p>
<p class="sub-links-paragraph">    <a class="sub-links-action" href="../REQQRYBROKERTRADINGALGOS/">ReqQryBrokerTradingAlgos</a></p>
<p class="sub-links-paragraph">    <a class="sub-links-action" href="../REQQRYBROKERTRADINGPARAMS/">ReqQryBrokerTradingParams</a></p>
<p class="sub-links-paragraph">    <a class="sub-links-action" href="../REQQRYCFMMCTRADINGACCOUNTKEY/">ReqQryCFMMCTradingAccountKey</a></p>
<p class="sub-links-paragraph">    <a class="sub-links-action" href="../REQQRYCOMBACTION/">ReqQryCombAction</a></p>
<p class="sub-links-paragraph">    <a class="sub-links-action" href="../REQQRYCOMBINSTRUMENTGUARD/">ReqQryCombInstrumentGuard</a></p>
<p class="sub-links-paragraph">    <a class="sub-links-action" href="../REQQRYCONTRACTBANK/">ReqQryContractBank</a></p>
<p class="sub-links-paragraph">    <a class="sub-links-action" href="../REQQRYDEPTHMARKETDATA/">ReqQryDepthMarketData</a></p>
<p class="sub-links-paragraph">    <a class="sub-links-action" href="../REQQRYEWARRANTOFFSET/">ReqQryEWarrantOffset</a></p>
<p class="sub-links-paragraph">    <a class="sub-links-action" href="../REQQRYEXCHANGE/">ReqQryExchange</a></p>
<p class="sub-links-paragraph">    <a class="sub-links-action" href="../REQQRYEXCHANGEMARGINRATE/">ReqQryExchangeMarginRate</a></p>
<p class="sub-links-paragraph">    <a class="sub-links-action" href="../REQQRYEXCHANGEMARGINRATEADJUST/">ReqQryExchangeMarginRateAdjust</a></p>
<p class="sub-links-paragraph">    <a class="sub-links-action" href="../REQQRYEXCHANGERATE/">ReqQryExchangeRate</a></p>
<p class="sub-links-paragraph">    <a class="sub-links-action" href="../REQQRYEXECORDER/">ReqQryExecOrder</a></p>
<p class="sub-links-paragraph">    <a class="sub-links-action" href="../REQQRYFORQUOTE/">ReqQryForQuote</a></p>
<p class="sub-links-paragraph">    <a class="sub-links-action" href="../REQQRYINSTRUMENT/">ReqQryInstrument</a></p>
<p class="sub-links-paragraph">    <a class="sub-links-action" href="../REQQRYINSTRUMENTCOMMISSIONRATE/">ReqQryInstrumentCommissionRate</a></p>
<p class="sub-links-paragraph">    <a class="sub-links-action" href="../REQQRYINSTRUMENTMARGINRATE/">ReqQryInstrumentMarginRate</a></p>
<p class="sub-links-paragraph">    <a class="sub-links-action" href="../REQQRYINSTRUMENTORDERCOMMRATE/">ReqQryInstrumentOrderCommRate</a></p>
<p class="sub-links-paragraph">    <a class="sub-links-action" href="../REQQRYINVESTOR/">ReqQryInvestor</a></p>
<p class="sub-links-paragraph">    <a class="sub-links-action" href="../REQQRYINVESTORPOSITION/">ReqQryInvestorPosition</a></p>
<p class="sub-links-paragraph">    <a class="sub-links-action" href="../REQQRYINVESTORPOSITIONCOMBINEDETAIL/">ReqQryInvestorPositionCombineDetail</a></p>
<p class="sub-links-paragraph">    <a class="sub-links-action" href="../REQQRYINVESTORPOSITIONDETAIL/">ReqQryInvestorPositionDetail</a></p>
<p class="sub-links-paragraph">    <a class="sub-links-action" href="../REQQRYINVESTORPRODUCTGROUPMARGIN/">ReqQryInvestorProductGroupMargin</a></p>
<p class="sub-links-paragraph">    <a class="sub-links-action" href="../REQQRYINVESTUNIT/">ReqQryInvestUnit</a></p>
<p class="sub-links-paragraph">    <a class="sub-links-action" href="../REQQRYMMINSTRUMENTCOMMISSIONRATE/">ReqQryMMInstrumentCommissionRate</a></p>
<p class="sub-links-paragraph">    <a class="sub-links-action" href="../REQQRYMMOPTIONINSTRCOMMRATE/">ReqQryMMOptionInstrCommRate</a></p>
<p class="sub-links-paragraph">    <a class="sub-links-action" href="../REQQRYNOTICE/">ReqQryNotice</a></p>
<p class="sub-links-paragraph">    <a class="sub-links-action" href="../REQQRYOPTIONINSTRCOMMRATE/">ReqQryOptionInstrCommRate</a></p>
<p class="sub-links-paragraph">    <a class="sub-links-action" href="../REQQRYOPTIONINSTRTRADECOST/">ReqQryOptionInstrTradeCost</a></p>
<p class="sub-links-paragraph">    <a class="sub-links-action" href="../REQQRYOPTIONSELFCLOSE/">ReqQryOptionSelfClose</a></p>
<p class="sub-links-paragraph">    <a class="sub-links-action" href="../REQQRYORDER/">ReqQryOrder</a></p>
<p class="sub-links-paragraph">    <a class="sub-links-action" href="../REQQRYPARKEDORDER/">ReqQryParkedOrder</a></p>
<p class="sub-links-paragraph">    <a class="sub-links-action" href="../REQQRYPARKEDORDERACTION/">ReqQryParkedOrderAction</a></p>
<p class="sub-links-paragraph">    <a class="sub-links-action" href="../REQQRYPRODUCT/">ReqQryProduct</a></p>
<p class="sub-links-paragraph">    <a class="sub-links-action" href="../REQQRYPRODUCTEXCHRATE/">ReqQryProductExchRate</a></p>
<p class="sub-links-paragraph">    <a class="sub-links-action" href="../REQQRYPRODUCTGROUP/">ReqQryProductGroup</a></p>
<p class="sub-links-paragraph">    <a class="sub-links-action" href="../REQQRYQUOTE/">ReqQryQuote</a></p>
<p class="sub-links-paragraph">    <a class="sub-links-action" href="../REQQRYSECAGENTACIDMAP/">ReqQrySecAgentACIDMap</a></p>
<p class="sub-links-paragraph">    <a class="sub-links-action" href="../REQQRYSECAGENTCHECKMODE/">ReqQrySecAgentCheckMode</a></p>
<p class="sub-links-paragraph">    <a class="sub-links-action" href="../REQQRYSECAGENTTRADEINFO/">ReqQrySecAgentTradeInfo</a></p>
<p class="sub-links-paragraph">    <a class="sub-links-action" href="../REQQRYSECAGENTTRADINGACCOUNT/">ReqQrySecAgentTradingAccount</a></p>
<p class="sub-links-paragraph">    <a class="sub-links-action" href="../REQQRYSETTLEMENTINFO/">ReqQrySettlementInfo</a></p>
<p class="sub-links-paragraph">    <a class="sub-links-action" href="../REQQRYSETTLEMENTINFOCONFIRM/">ReqQrySettlementInfoConfirm</a></p>
<p class="sub-links-paragraph">    <a class="sub-links-action" href="../REQQRYTRADE/">ReqQryTrade</a></p>
<p class="sub-links-paragraph">    <a class="sub-links-action" href="../REQQRYTRADINGACCOUNT/">ReqQryTradingAccount</a></p>
<p class="sub-links-paragraph">    <a class="sub-links-action" href="../REQQRYTRADINGCODE/">ReqQryTradingCode</a></p>
<p class="sub-links-paragraph">    <a class="sub-links-action" href="../REQQRYTRADINGNOTICE/">ReqQryTradingNotice</a></p>
<p class="sub-links-paragraph">    <a class="sub-links-action" href="../REQQRYTRANSFERBANK/">ReqQryTransferBank</a></p>
<p class="sub-links-paragraph">    <a class="sub-links-action" href="../REQQRYTRANSFERSERIAL/">ReqQryTransferSerial</a></p>
<p class="sub-links-paragraph">    <a class="sub-links-action" href="../REQQUERYBANKACCOUNTMONEYBYFUTURE/">ReqQueryBankAccountMoneyByFuture</a></p>
<p class="sub-links-paragraph">    <a class="sub-links-action" href="../REQQUERYCFMMCTRADINGACCOUNTTOKEN/">ReqQueryCFMMCTradingAccountToken</a></p>
<p class="sub-links-paragraph">    <a class="sub-links-action" href="../REQQUERYMAXORDERVOLUME/">ReqQueryMaxOrderVolume</a></p>
<p class="sub-links-paragraph">    <a class="sub-links-action" href="../REQQUOTEACTION/">ReqQuoteAction</a></p>
<p class="sub-links-paragraph">    <a class="sub-links-action" href="../REQQUOTEINSERT/">ReqQuoteInsert</a></p>
<p class="sub-links-paragraph">    <a class="sub-links-action" href="../REQREMOVEPARKEDORDER/">ReqRemoveParkedOrder</a></p>
<p class="sub-links-paragraph">    <a class="sub-links-action" href="../REQREMOVEPARKEDORDERACTION/">ReqRemoveParkedOrderAction</a></p>
<p class="sub-links-paragraph">    <a class="sub-links-action" href="../REQSETTLEMENTINFOCONFIRM/">ReqSettlementInfoConfirm</a></p>
<p class="sub-links-paragraph">    <a class="sub-links-action" href="../REQTRADINGACCOUNTPASSWORDUPDATE/">ReqTradingAccountPasswordUpdate</a></p>
<p class="sub-links-paragraph">    <a class="sub-links-action" href="../REQUSERAUTHMETHOD/">ReqUserAuthMethod</a></p>
<p class="sub-links-paragraph">    <a class="sub-links-action" href="../REQUSERLOGIN/">ReqUserLogin</a></p>
<p class="sub-links-paragraph">    <a class="sub-links-action" href="../REQUSERLOGINWITHCAPTCHA/">ReqUserLoginWithCaptcha</a></p>
<p class="sub-links-paragraph">    <a class="sub-links-action" href="../REQUSERLOGINWITHOTP/">ReqUserLoginWithOTP</a></p>
<p class="sub-links-paragraph">    <a class="sub-links-action" href="../REQUSERLOGINWITHTEXT/">ReqUserLoginWithText</a></p>
<p class="sub-links-paragraph">    <a class="sub-links-action" href="../REQUSERLOGOUT/">ReqUserLogout</a></p>
<p class="sub-links-paragraph">    <a class="sub-links-action" href="../REQUSERPASSWORDUPDATE/">ReqUserPasswordUpdate</a></p>
<p class="sub-links-paragraph">    <a class="sub-links-action" href="../SUBMITUSERSYSTEMINFO/">SubmitUserSystemInfo</a></p>
<p class="sub-links-paragraph">    <a class="sub-links-action" href="../SUBSCRIBEPRIVATETOPIC/">SubscribePrivateTopic</a></p>
<p class="sub-links-paragraph">    <a class="sub-links-action" href="../SUBSCRIBEPUBLICTOPIC/">SubscribePublicTopic</a></p>
</div>
