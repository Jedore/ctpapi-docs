<table border="0" cellspacing="0" class="square-block" id=""><tbody border="0"><tr border="0"><td class="square-block-left"></td><td class="square-block-content"><div>

</div></td><td class="square-block-right"></td></tr></tbody></table>
<p>CThostFtdcTraderSpi类提供了交易相关的回调接口，用户需要继承该类并重载这些接口，以获取响应数据。</p>
<span class="anchor" id="d74f0097-e68f-4399-8c26-0da88c6a61cf"></span>
## 1.接口
<pre><code>class CThostFtdcTraderSpi
{
public:
    ///当客户端与交易后台建立起通信连接时（还未登录前），该方法被调用。
    virtual void OnFrontConnected(){};
    ///当客户端与交易后台通信连接断开时，该方法被调用。当发生这个情况后，API会自动重新连接，客户端可不做处理。
    ///@param nReason 错误原因
    ///        0x1001 网络读失败
    ///        0x1002 网络写失败
    ///        0x2001 接收心跳超时
    ///        0x2002 发送心跳失败
    ///        0x2003 收到错误报文
    virtual void OnFrontDisconnected(int nReason){};
    ///心跳超时警告。当长时间未收到报文时，该方法被调用。
    ///@param nTimeLapse 距离上次接收报文的时间
    virtual void OnHeartBeatWarning(int nTimeLapse){};
    ///客户端认证响应
    virtual void OnRspAuthenticate(CThostFtdcRspAuthenticateField *pRspAuthenticateField, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};
    ///登录请求响应
    virtual void OnRspUserLogin(CThostFtdcRspUserLoginField *pRspUserLogin, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};
    ///登出请求响应
    virtual void OnRspUserLogout(CThostFtdcUserLogoutField *pUserLogout, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};
    ///用户口令更新请求响应
    virtual void OnRspUserPasswordUpdate(CThostFtdcUserPasswordUpdateField *pUserPasswordUpdate, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};
    ///资金账户口令更新请求响应
    virtual void OnRspTradingAccountPasswordUpdate(CThostFtdcTradingAccountPasswordUpdateField *pTradingAccountPasswordUpdate, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};
    ///查询用户当前支持的认证模式的回复
    virtual void OnRspUserAuthMethod(CThostFtdcRspUserAuthMethodField *pRspUserAuthMethod, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};
    ///获取图形验证码请求的回复
    virtual void OnRspGenUserCaptcha(CThostFtdcRspGenUserCaptchaField *pRspGenUserCaptcha, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};
    ///获取短信验证码请求的回复
    virtual void OnRspGenUserText(CThostFtdcRspGenUserTextField *pRspGenUserText, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};
    ///报单录入请求响应
    virtual void OnRspOrderInsert(CThostFtdcInputOrderField *pInputOrder, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};
    ///预埋单录入请求响应
    virtual void OnRspParkedOrderInsert(CThostFtdcParkedOrderField *pParkedOrder, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};
    ///预埋撤单录入请求响应
    virtual void OnRspParkedOrderAction(CThostFtdcParkedOrderActionField *pParkedOrderAction, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};
    ///报单操作请求响应
    virtual void OnRspOrderAction(CThostFtdcInputOrderActionField *pInputOrderAction, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};
    ///查询最大报单数量响应
    virtual void OnRspQueryMaxOrderVolume(CThostFtdcQueryMaxOrderVolumeField *pQueryMaxOrderVolume, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};
    ///投资者结算结果确认响应
    virtual void OnRspSettlementInfoConfirm(CThostFtdcSettlementInfoConfirmField *pSettlementInfoConfirm, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};
    ///删除预埋单响应
    virtual void OnRspRemoveParkedOrder(CThostFtdcRemoveParkedOrderField *pRemoveParkedOrder, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};
    ///删除预埋撤单响应
    virtual void OnRspRemoveParkedOrderAction(CThostFtdcRemoveParkedOrderActionField *pRemoveParkedOrderAction, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};
    ///执行宣告录入请求响应
    virtual void OnRspExecOrderInsert(CThostFtdcInputExecOrderField *pInputExecOrder, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};
    ///执行宣告操作请求响应
    virtual void OnRspExecOrderAction(CThostFtdcInputExecOrderActionField *pInputExecOrderAction, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};
    ///询价录入请求响应
    virtual void OnRspForQuoteInsert(CThostFtdcInputForQuoteField *pInputForQuote, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};
    ///报价录入请求响应
    virtual void OnRspQuoteInsert(CThostFtdcInputQuoteField *pInputQuote, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};
    ///报价操作请求响应
    virtual void OnRspQuoteAction(CThostFtdcInputQuoteActionField *pInputQuoteAction, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};
    ///批量报单操作请求响应
    virtual void OnRspBatchOrderAction(CThostFtdcInputBatchOrderActionField *pInputBatchOrderAction, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};
    ///期权自对冲录入请求响应
    virtual void OnRspOptionSelfCloseInsert(CThostFtdcInputOptionSelfCloseField *pInputOptionSelfClose, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};
    ///期权自对冲操作请求响应
    virtual void OnRspOptionSelfCloseAction(CThostFtdcInputOptionSelfCloseActionField *pInputOptionSelfCloseAction, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};
    ///申请组合录入请求响应
    virtual void OnRspCombActionInsert(CThostFtdcInputCombActionField *pInputCombAction, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};
    ///请求查询报单响应
    virtual void OnRspQryOrder(CThostFtdcOrderField *pOrder, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};
    ///请求查询成交响应
    virtual void OnRspQryTrade(CThostFtdcTradeField *pTrade, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};
    ///请求查询投资者持仓响应
    virtual void OnRspQryInvestorPosition(CThostFtdcInvestorPositionField *pInvestorPosition, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};
    ///请求查询资金账户响应
    virtual void OnRspQryTradingAccount(CThostFtdcTradingAccountField *pTradingAccount, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};
    ///请求查询投资者响应
    virtual void OnRspQryInvestor(CThostFtdcInvestorField *pInvestor, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};
    ///请求查询交易编码响应
    virtual void OnRspQryTradingCode(CThostFtdcTradingCodeField *pTradingCode, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};
    ///请求查询合约保证金率响应
    virtual void OnRspQryInstrumentMarginRate(CThostFtdcInstrumentMarginRateField *pInstrumentMarginRate, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};
    ///请求查询合约手续费率响应
    virtual void OnRspQryInstrumentCommissionRate(CThostFtdcInstrumentCommissionRateField *pInstrumentCommissionRate, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};
    ///请求查询交易所响应
    virtual void OnRspQryExchange(CThostFtdcExchangeField *pExchange, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};
    ///请求查询产品响应
    virtual void OnRspQryProduct(CThostFtdcProductField *pProduct, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};
    ///请求查询合约响应
    virtual void OnRspQryInstrument(CThostFtdcInstrumentField *pInstrument, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};
    ///请求查询行情响应
    virtual void OnRspQryDepthMarketData(CThostFtdcDepthMarketDataField *pDepthMarketData, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};
    ///请求查询投资者结算结果响应
    virtual void OnRspQrySettlementInfo(CThostFtdcSettlementInfoField *pSettlementInfo, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};
    ///请求查询转帐银行响应
    virtual void OnRspQryTransferBank(CThostFtdcTransferBankField *pTransferBank, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};
    ///请求查询投资者持仓明细响应
    virtual void OnRspQryInvestorPositionDetail(CThostFtdcInvestorPositionDetailField *pInvestorPositionDetail, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};
    ///请求查询客户通知响应
    virtual void OnRspQryNotice(CThostFtdcNoticeField *pNotice, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};
    ///请求查询结算信息确认响应
    virtual void OnRspQrySettlementInfoConfirm(CThostFtdcSettlementInfoConfirmField *pSettlementInfoConfirm, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};
    ///请求查询投资者持仓明细响应
    virtual void OnRspQryInvestorPositionCombineDetail(CThostFtdcInvestorPositionCombineDetailField *pInvestorPositionCombineDetail, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};
    ///查询保证金监管系统经纪公司资金账户密钥响应
    virtual void OnRspQryCFMMCTradingAccountKey(CThostFtdcCFMMCTradingAccountKeyField *pCFMMCTradingAccountKey, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};
    ///请求查询仓单折抵信息响应
    virtual void OnRspQryEWarrantOffset(CThostFtdcEWarrantOffsetField *pEWarrantOffset, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};
    ///请求查询投资者品种/跨品种保证金响应
    virtual void OnRspQryInvestorProductGroupMargin(CThostFtdcInvestorProductGroupMarginField *pInvestorProductGroupMargin, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};
    ///请求查询交易所保证金率响应
    virtual void OnRspQryExchangeMarginRate(CThostFtdcExchangeMarginRateField *pExchangeMarginRate, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};
    ///请求查询交易所调整保证金率响应
    virtual void OnRspQryExchangeMarginRateAdjust(CThostFtdcExchangeMarginRateAdjustField *pExchangeMarginRateAdjust, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};
    ///请求查询汇率响应
    virtual void OnRspQryExchangeRate(CThostFtdcExchangeRateField *pExchangeRate, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};
    ///请求查询二级代理操作员银期权限响应
    virtual void OnRspQrySecAgentACIDMap(CThostFtdcSecAgentACIDMapField *pSecAgentACIDMap, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};
    ///请求查询产品报价汇率
    virtual void OnRspQryProductExchRate(CThostFtdcProductExchRateField *pProductExchRate, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};
    ///请求查询产品组
    virtual void OnRspQryProductGroup(CThostFtdcProductGroupField *pProductGroup, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};
    ///请求查询做市商合约手续费率响应
    virtual void OnRspQryMMInstrumentCommissionRate(CThostFtdcMMInstrumentCommissionRateField *pMMInstrumentCommissionRate, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};
    ///请求查询做市商期权合约手续费响应
    virtual void OnRspQryMMOptionInstrCommRate(CThostFtdcMMOptionInstrCommRateField *pMMOptionInstrCommRate, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};
    ///请求查询报单手续费响应
    virtual void OnRspQryInstrumentOrderCommRate(CThostFtdcInstrumentOrderCommRateField *pInstrumentOrderCommRate, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};
    ///请求查询资金账户响应
    virtual void OnRspQrySecAgentTradingAccount(CThostFtdcTradingAccountField *pTradingAccount, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};
    ///请求查询二级代理商资金校验模式响应
    virtual void OnRspQrySecAgentCheckMode(CThostFtdcSecAgentCheckModeField *pSecAgentCheckMode, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};
    ///请求查询二级代理商信息响应
    virtual void OnRspQrySecAgentTradeInfo(CThostFtdcSecAgentTradeInfoField *pSecAgentTradeInfo, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};
    ///请求查询期权交易成本响应
    virtual void OnRspQryOptionInstrTradeCost(CThostFtdcOptionInstrTradeCostField *pOptionInstrTradeCost, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};
    ///请求查询期权合约手续费响应
    virtual void OnRspQryOptionInstrCommRate(CThostFtdcOptionInstrCommRateField *pOptionInstrCommRate, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};
    ///请求查询执行宣告响应
    virtual void OnRspQryExecOrder(CThostFtdcExecOrderField *pExecOrder, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};
    ///请求查询询价响应
    virtual void OnRspQryForQuote(CThostFtdcForQuoteField *pForQuote, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};
    ///请求查询报价响应
    virtual void OnRspQryQuote(CThostFtdcQuoteField *pQuote, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};
    ///请求查询期权自对冲响应
    virtual void OnRspQryOptionSelfClose(CThostFtdcOptionSelfCloseField *pOptionSelfClose, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};
    ///请求查询投资单元响应
    virtual void OnRspQryInvestUnit(CThostFtdcInvestUnitField *pInvestUnit, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};
    ///请求查询组合合约安全系数响应
    virtual void OnRspQryCombInstrumentGuard(CThostFtdcCombInstrumentGuardField *pCombInstrumentGuard, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};
    ///请求查询申请组合响应
    virtual void OnRspQryCombAction(CThostFtdcCombActionField *pCombAction, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};
    ///请求查询转帐流水响应
    virtual void OnRspQryTransferSerial(CThostFtdcTransferSerialField *pTransferSerial, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};
    ///请求查询银期签约关系响应
    virtual void OnRspQryAccountregister(CThostFtdcAccountregisterField *pAccountregister, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};
    ///错误应答
    virtual void OnRspError(CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};
    ///报单通知
    virtual void OnRtnOrder(CThostFtdcOrderField *pOrder) {};
    ///成交通知
    virtual void OnRtnTrade(CThostFtdcTradeField *pTrade) {};
    ///报单录入错误回报
    virtual void OnErrRtnOrderInsert(CThostFtdcInputOrderField *pInputOrder, CThostFtdcRspInfoField *pRspInfo) {};
    ///报单操作错误回报
    virtual void OnErrRtnOrderAction(CThostFtdcOrderActionField *pOrderAction, CThostFtdcRspInfoField *pRspInfo) {};
    ///合约交易状态通知
    virtual void OnRtnInstrumentStatus(CThostFtdcInstrumentStatusField *pInstrumentStatus) {};
    ///交易所公告通知
    virtual void OnRtnBulletin(CThostFtdcBulletinField *pBulletin) {};
    ///交易通知
    virtual void OnRtnTradingNotice(CThostFtdcTradingNoticeInfoField *pTradingNoticeInfo) {};
    ///提示条件单校验错误
    virtual void OnRtnErrorConditionalOrder(CThostFtdcErrorConditionalOrderField *pErrorConditionalOrder) {};
    ///执行宣告通知
    virtual void OnRtnExecOrder(CThostFtdcExecOrderField *pExecOrder) {};
    ///执行宣告录入错误回报
    virtual void OnErrRtnExecOrderInsert(CThostFtdcInputExecOrderField *pInputExecOrder, CThostFtdcRspInfoField *pRspInfo) {};
    ///执行宣告操作错误回报
    virtual void OnErrRtnExecOrderAction(CThostFtdcExecOrderActionField *pExecOrderAction, CThostFtdcRspInfoField *pRspInfo) {};
    ///询价录入错误回报
    virtual void OnErrRtnForQuoteInsert(CThostFtdcInputForQuoteField *pInputForQuote, CThostFtdcRspInfoField *pRspInfo) {};
    ///报价通知
    virtual void OnRtnQuote(CThostFtdcQuoteField *pQuote) {};
    ///报价录入错误回报
    virtual void OnErrRtnQuoteInsert(CThostFtdcInputQuoteField *pInputQuote, CThostFtdcRspInfoField *pRspInfo) {};
    ///报价操作错误回报
    virtual void OnErrRtnQuoteAction(CThostFtdcQuoteActionField *pQuoteAction, CThostFtdcRspInfoField *pRspInfo) {};
    ///询价通知
    virtual void OnRtnForQuoteRsp(CThostFtdcForQuoteRspField *pForQuoteRsp) {};
    ///保证金监控中心用户令牌
    virtual void OnRtnCFMMCTradingAccountToken(CThostFtdcCFMMCTradingAccountTokenField *pCFMMCTradingAccountToken) {};
    ///批量报单操作错误回报
    virtual void OnErrRtnBatchOrderAction(CThostFtdcBatchOrderActionField *pBatchOrderAction, CThostFtdcRspInfoField *pRspInfo) {};
    ///期权自对冲通知
    virtual void OnRtnOptionSelfClose(CThostFtdcOptionSelfCloseField *pOptionSelfClose) {};
    ///期权自对冲录入错误回报
    virtual void OnErrRtnOptionSelfCloseInsert(CThostFtdcInputOptionSelfCloseField *pInputOptionSelfClose, CThostFtdcRspInfoField *pRspInfo) {};
    ///期权自对冲操作错误回报
    virtual void OnErrRtnOptionSelfCloseAction(CThostFtdcOptionSelfCloseActionField *pOptionSelfCloseAction, CThostFtdcRspInfoField *pRspInfo) {};
    ///申请组合通知
    virtual void OnRtnCombAction(CThostFtdcCombActionField *pCombAction) {};
    ///申请组合录入错误回报
    virtual void OnErrRtnCombActionInsert(CThostFtdcInputCombActionField *pInputCombAction, CThostFtdcRspInfoField *pRspInfo) {};
    ///请求查询签约银行响应
    virtual void OnRspQryContractBank(CThostFtdcContractBankField *pContractBank, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};
    ///请求查询预埋单响应
    virtual void OnRspQryParkedOrder(CThostFtdcParkedOrderField *pParkedOrder, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};
    ///请求查询预埋撤单响应
    virtual void OnRspQryParkedOrderAction(CThostFtdcParkedOrderActionField *pParkedOrderAction, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};
    ///请求查询交易通知响应
    virtual void OnRspQryTradingNotice(CThostFtdcTradingNoticeField *pTradingNotice, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};
    ///请求查询经纪公司交易参数响应
    virtual void OnRspQryBrokerTradingParams(CThostFtdcBrokerTradingParamsField *pBrokerTradingParams, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};
    ///请求查询经纪公司交易算法响应
    virtual void OnRspQryBrokerTradingAlgos(CThostFtdcBrokerTradingAlgosField *pBrokerTradingAlgos, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};
    ///请求查询监控中心用户令牌
    virtual void OnRspQueryCFMMCTradingAccountToken(CThostFtdcQueryCFMMCTradingAccountTokenField *pQueryCFMMCTradingAccountToken, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};
    ///银行发起银行资金转期货通知
    virtual void OnRtnFromBankToFutureByBank(CThostFtdcRspTransferField *pRspTransfer) {};
    ///银行发起期货资金转银行通知
    virtual void OnRtnFromFutureToBankByBank(CThostFtdcRspTransferField *pRspTransfer) {};
    ///银行发起冲正银行转期货通知
    virtual void OnRtnRepealFromBankToFutureByBank(CThostFtdcRspRepealField *pRspRepeal) {};
    ///银行发起冲正期货转银行通知
    virtual void OnRtnRepealFromFutureToBankByBank(CThostFtdcRspRepealField *pRspRepeal) {};
    ///期货发起银行资金转期货通知
    virtual void OnRtnFromBankToFutureByFuture(CThostFtdcRspTransferField *pRspTransfer) {};
    ///期货发起期货资金转银行通知
    virtual void OnRtnFromFutureToBankByFuture(CThostFtdcRspTransferField *pRspTransfer) {};
    ///系统运行时期货端手工发起冲正银行转期货请求，银行处理完毕后报盘发回的通知
    virtual void OnRtnRepealFromBankToFutureByFutureManual(CThostFtdcRspRepealField *pRspRepeal) {};
    ///系统运行时期货端手工发起冲正期货转银行请求，银行处理完毕后报盘发回的通知
    virtual void OnRtnRepealFromFutureToBankByFutureManual(CThostFtdcRspRepealField *pRspRepeal) {};
    ///期货发起查询银行余额通知
    virtual void OnRtnQueryBankBalanceByFuture(CThostFtdcNotifyQueryAccountField *pNotifyQueryAccount) {};
    ///期货发起银行资金转期货错误回报
    virtual void OnErrRtnBankToFutureByFuture(CThostFtdcReqTransferField *pReqTransfer, CThostFtdcRspInfoField *pRspInfo) {};
    ///期货发起期货资金转银行错误回报
    virtual void OnErrRtnFutureToBankByFuture(CThostFtdcReqTransferField *pReqTransfer, CThostFtdcRspInfoField *pRspInfo) {};
    ///系统运行时期货端手工发起冲正银行转期货错误回报
    virtual void OnErrRtnRepealBankToFutureByFutureManual(CThostFtdcReqRepealField *pReqRepeal, CThostFtdcRspInfoField *pRspInfo) {};
    ///系统运行时期货端手工发起冲正期货转银行错误回报
    virtual void OnErrRtnRepealFutureToBankByFutureManual(CThostFtdcReqRepealField *pReqRepeal, CThostFtdcRspInfoField *pRspInfo) {};
    ///期货发起查询银行余额错误回报
    virtual void OnErrRtnQueryBankBalanceByFuture(CThostFtdcReqQueryAccountField *pReqQueryAccount, CThostFtdcRspInfoField *pRspInfo) {};
    ///期货发起冲正银行转期货请求，银行处理完毕后报盘发回的通知
    virtual void OnRtnRepealFromBankToFutureByFuture(CThostFtdcRspRepealField *pRspRepeal) {};
    ///期货发起冲正期货转银行请求，银行处理完毕后报盘发回的通知
    virtual void OnRtnRepealFromFutureToBankByFuture(CThostFtdcRspRepealField *pRspRepeal) {};
    ///期货发起银行资金转期货应答
    virtual void OnRspFromBankToFutureByFuture(CThostFtdcReqTransferField *pReqTransfer, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};
    ///期货发起期货资金转银行应答
    virtual void OnRspFromFutureToBankByFuture(CThostFtdcReqTransferField *pReqTransfer, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};
    ///期货发起查询银行余额应答
    virtual void OnRspQueryBankAccountMoneyByFuture(CThostFtdcReqQueryAccountField *pReqQueryAccount, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};
    ///银行发起银期开户通知
    virtual void OnRtnOpenAccountByBank(CThostFtdcOpenAccountField *pOpenAccount) {};
    ///银行发起银期销户通知
    virtual void OnRtnCancelAccountByBank(CThostFtdcCancelAccountField *pCancelAccount) {};
    ///银行发起变更银行账号通知
    virtual void OnRtnChangeAccountByBank(CThostFtdcChangeAccountField *pChangeAccount) {};
};
</code></pre>
<span class="anchor" id="b09daeb9-7bf1-4642-9ed8-d8f1ae2ae479"></span>
## 2.代码示例
<pre><code>// CTraderHandler继承CThostFtdcTraderSpi
class CTraderHandler : public CThostFtdcTraderSpi
{
  //重载，报单通知
  void OnRtnOrder(CThostFtdcOrderField *pOrder)
  {
      printf("OnRtnOrder\n");
  }
  //重载，成交通知
  void OnRtnTrade(CThostFtdcTradeField *pTrade)
  {
      printf("OnRtnTrade\n");
  }
  //重载，报单录入请求响应
  void OnRspOrderInsert(CThostFtdcInputOrderField *pInputOrder, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
  {
      printf("OnRspOrderInsert\n");
  }
  //重载，错误应答
  void OnRspError(CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
  {
      printf("OnRspError\n");
  }
}
</code></pre>
<span class="anchor" id="c58831c5-ed3a-4c14-8049-c821920b6323"></span>
## 3.FAQ
<p>无</p>
<div class="sub-links-list" style="text-indent:0px;"><hr class="SubLinksListLine"/>
<p class="sub-links-list-header">请参阅：</p>
<p class="sub-links-paragraph">    <a class="sub-links-action" href="../ONERRRTNBANKTOFUTUREBYFUTURE/">OnErrRtnBankToFutureByFuture</a></p>
<p class="sub-links-paragraph">    <a class="sub-links-action" href="../ONERRRTNBATCHORDERACTION/">OnErrRtnBatchOrderAction</a></p>
<p class="sub-links-paragraph">    <a class="sub-links-action" href="../ONERRRTNCOMBACTIONINSERT/">OnErrRtnCombActionInsert</a></p>
<p class="sub-links-paragraph">    <a class="sub-links-action" href="../ONERRRTNEXECORDERACTION/">OnErrRtnExecOrderAction</a></p>
<p class="sub-links-paragraph">    <a class="sub-links-action" href="../ONERRRTNEXECORDERINSERT/">OnErrRtnExecOrderInsert</a></p>
<p class="sub-links-paragraph">    <a class="sub-links-action" href="../ONERRRTNFORQUOTEINSERT/">OnErrRtnForQuoteInsert</a></p>
<p class="sub-links-paragraph">    <a class="sub-links-action" href="../ONERRRTNFUTURETOBANKBYFUTURE/">OnErrRtnFutureToBankByFuture</a></p>
<p class="sub-links-paragraph">    <a class="sub-links-action" href="../ONERRRTNOPTIONSELFCLOSEACTION/">OnErrRtnOptionSelfCloseAction</a></p>
<p class="sub-links-paragraph">    <a class="sub-links-action" href="../ONERRRTNOPTIONSELFCLOSEINSERT/">OnErrRtnOptionSelfCloseInsert</a></p>
<p class="sub-links-paragraph">    <a class="sub-links-action" href="../ONERRRTNORDERACTION/">OnErrRtnOrderAction</a></p>
<p class="sub-links-paragraph">    <a class="sub-links-action" href="../ONERRRTNORDERINSERT/">OnErrRtnOrderInsert</a></p>
<p class="sub-links-paragraph">    <a class="sub-links-action" href="../ONERRRTNQUERYBANKBALANCEBYFUTURE/">OnErrRtnQueryBankBalanceByFuture</a></p>
<p class="sub-links-paragraph">    <a class="sub-links-action" href="../ONERRRTNQUOTEACTION/">OnErrRtnQuoteAction</a></p>
<p class="sub-links-paragraph">    <a class="sub-links-action" href="../ONERRRTNQUOTEINSERT/">OnErrRtnQuoteInsert</a></p>
<p class="sub-links-paragraph">    <a class="sub-links-action" href="../ONERRRTNREPEALBANKTOFUTUREBYFUTUREMANUAL/">OnErrRtnRepealBankToFutureByFutureManual</a></p>
<p class="sub-links-paragraph">    <a class="sub-links-action" href="../ONERRRTNREPEALFUTURETOBANKBYFUTUREMANUAL/">OnErrRtnRepealFutureToBankByFutureManual</a></p>
<p class="sub-links-paragraph">    <a class="sub-links-action" href="../ONFRONTCONNECTED/">OnFrontConnected</a></p>
<p class="sub-links-paragraph">    <a class="sub-links-action" href="../ONFRONTDISCONNECTED/">OnFrontDisconnected</a></p>
<p class="sub-links-paragraph">    <a class="sub-links-action" href="../ONHEARTBEATWARNING/">OnHeartBeatWarning</a></p>
<p class="sub-links-paragraph">    <a class="sub-links-action" href="../ONRSPAUTHENTICATE/">OnRspAuthenticate</a></p>
<p class="sub-links-paragraph">    <a class="sub-links-action" href="../ONRSPBATCHORDERACTION/">OnRspBatchOrderAction</a></p>
<p class="sub-links-paragraph">    <a class="sub-links-action" href="../ONRSPCOMBACTIONINSERT/">OnRspCombActionInsert</a></p>
<p class="sub-links-paragraph">    <a class="sub-links-action" href="../ONRSPERROR/">OnRspError</a></p>
<p class="sub-links-paragraph">    <a class="sub-links-action" href="../ONRSPEXECORDERACTION/">OnRspExecOrderAction</a></p>
<p class="sub-links-paragraph">    <a class="sub-links-action" href="../ONRSPEXECORDERINSERT/">OnRspExecOrderInsert</a></p>
<p class="sub-links-paragraph">    <a class="sub-links-action" href="../ONRSPFORQUOTEINSERT/">OnRspForQuoteInsert</a></p>
<p class="sub-links-paragraph">    <a class="sub-links-action" href="../ONRSPFROMBANKTOFUTUREBYFUTURE/">OnRspFromBankToFutureByFuture</a></p>
<p class="sub-links-paragraph">    <a class="sub-links-action" href="../ONRSPFROMFUTURETOBANKBYFUTURE/">OnRspFromFutureToBankByFuture</a></p>
<p class="sub-links-paragraph">    <a class="sub-links-action" href="../ONRSPGENUSERCAPTCHA/">OnRspGenUserCaptcha</a></p>
<p class="sub-links-paragraph">    <a class="sub-links-action" href="../ONRSPGENUSERTEXT/">OnRspGenUserText</a></p>
<p class="sub-links-paragraph">    <a class="sub-links-action" href="../ONRSPOPTIONSELFCLOSEACTION/">OnRspOptionSelfCloseAction</a></p>
<p class="sub-links-paragraph">    <a class="sub-links-action" href="../ONRSPOPTIONSELFCLOSEINSERT/">OnRspOptionSelfCloseInsert</a></p>
<p class="sub-links-paragraph">    <a class="sub-links-action" href="../ONRSPORDERACTION/">OnRspOrderAction</a></p>
<p class="sub-links-paragraph">    <a class="sub-links-action" href="../ONRSPORDERINSERT/">OnRspOrderInsert</a></p>
<p class="sub-links-paragraph">    <a class="sub-links-action" href="../ONRSPPARKEDORDERACTION/">OnRspParkedOrderAction</a></p>
<p class="sub-links-paragraph">    <a class="sub-links-action" href="../ONRSPPARKEDORDERINSERT/">OnRspParkedOrderInsert</a></p>
<p class="sub-links-paragraph">    <a class="sub-links-action" href="../ONRSPQRYACCOUNTREGISTER/">OnRspQryAccountregister</a></p>
<p class="sub-links-paragraph">    <a class="sub-links-action" href="../ONRSPQRYBROKERTRADINGALGOS/">OnRspQryBrokerTradingAlgos</a></p>
<p class="sub-links-paragraph">    <a class="sub-links-action" href="../ONRSPQRYBROKERTRADINGPARAMS/">OnRspQryBrokerTradingParams</a></p>
<p class="sub-links-paragraph">    <a class="sub-links-action" href="../ONRSPQRYCFMMCTRADINGACCOUNTKEY/">OnRspQryCFMMCTradingAccountKey</a></p>
<p class="sub-links-paragraph">    <a class="sub-links-action" href="../ONRSPQRYCOMBACTION/">OnRspQryCombAction</a></p>
<p class="sub-links-paragraph">    <a class="sub-links-action" href="../ONRSPQRYCOMBINSTRUMENTGUARD/">OnRspQryCombInstrumentGuard</a></p>
<p class="sub-links-paragraph">    <a class="sub-links-action" href="../ONRSPQRYCONTRACTBANK/">OnRspQryContractBank</a></p>
<p class="sub-links-paragraph">    <a class="sub-links-action" href="../ONRSPQRYDEPTHMARKETDATA/">OnRspQryDepthMarketData</a></p>
<p class="sub-links-paragraph">    <a class="sub-links-action" href="../ONRSPQRYEWARRANTOFFSET/">OnRspQryEWarrantOffset</a></p>
<p class="sub-links-paragraph">    <a class="sub-links-action" href="../ONRSPQRYEXCHANGE/">OnRspQryExchange</a></p>
<p class="sub-links-paragraph">    <a class="sub-links-action" href="../ONRSPQRYEXCHANGEMARGINRATE/">OnRspQryExchangeMarginRate</a></p>
<p class="sub-links-paragraph">    <a class="sub-links-action" href="../ONRSPQRYEXCHANGEMARGINRATEADJUST/">OnRspQryExchangeMarginRateAdjust</a></p>
<p class="sub-links-paragraph">    <a class="sub-links-action" href="../ONRSPQRYEXCHANGERATE/">OnRspQryExchangeRate</a></p>
<p class="sub-links-paragraph">    <a class="sub-links-action" href="../ONRSPQRYEXECORDER/">OnRspQryExecOrder</a></p>
<p class="sub-links-paragraph">    <a class="sub-links-action" href="../ONRSPQRYFORQUOTE/">OnRspQryForQuote</a></p>
<p class="sub-links-paragraph">    <a class="sub-links-action" href="../ONRSPQRYINSTRUMENT/">OnRspQryInstrument</a></p>
<p class="sub-links-paragraph">    <a class="sub-links-action" href="../ONRSPQRYINSTRUMENTCOMMISSIONRATE/">OnRspQryInstrumentCommissionRate</a></p>
<p class="sub-links-paragraph">    <a class="sub-links-action" href="../ONRSPQRYINSTRUMENTMARGINRATE/">OnRspQryInstrumentMarginRate</a></p>
<p class="sub-links-paragraph">    <a class="sub-links-action" href="../ONRSPQRYINSTRUMENTORDERCOMMRATE/">OnRspQryInstrumentOrderCommRate</a></p>
<p class="sub-links-paragraph">    <a class="sub-links-action" href="../ONRSPQRYINVESTOR/">OnRspQryInvestor</a></p>
<p class="sub-links-paragraph">    <a class="sub-links-action" href="../ONRSPQRYINVESTORPOSITION/">OnRspQryInvestorPosition</a></p>
<p class="sub-links-paragraph">    <a class="sub-links-action" href="../ONRSPQRYINVESTORPOSITIONCOMBINEDETAIL/">OnRspQryInvestorPositionCombineDetail</a></p>
<p class="sub-links-paragraph">    <a class="sub-links-action" href="../ONRSPQRYINVESTORPOSITIONDETAIL/">OnRspQryInvestorPositionDetail</a></p>
<p class="sub-links-paragraph">    <a class="sub-links-action" href="../ONRSPQRYINVESTORPRODUCTGROUPMARGIN/">OnRspQryInvestorProductGroupMargin</a></p>
<p class="sub-links-paragraph">    <a class="sub-links-action" href="../ONRSPQRYINVESTUNIT/">OnRspQryInvestUnit</a></p>
<p class="sub-links-paragraph">    <a class="sub-links-action" href="../ONRSPQRYMMINSTRUMENTCOMMISSIONRATE/">OnRspQryMMInstrumentCommissionRate</a></p>
<p class="sub-links-paragraph">    <a class="sub-links-action" href="../ONRSPQRYMMOPTIONINSTRCOMMRATE/">OnRspQryMMOptionInstrCommRate</a></p>
<p class="sub-links-paragraph">    <a class="sub-links-action" href="../ONRSPQRYNOTICE/">OnRspQryNotice</a></p>
<p class="sub-links-paragraph">    <a class="sub-links-action" href="../ONRSPQRYOPTIONINSTRCOMMRATE/">OnRspQryOptionInstrCommRate</a></p>
<p class="sub-links-paragraph">    <a class="sub-links-action" href="../ONRSPQRYOPTIONINSTRTRADECOST/">OnRspQryOptionInstrTradeCost</a></p>
<p class="sub-links-paragraph">    <a class="sub-links-action" href="../ONRSPQRYOPTIONSELFCLOSE/">OnRspQryOptionSelfClose</a></p>
<p class="sub-links-paragraph">    <a class="sub-links-action" href="../ONRSPQRYORDER/">OnRspQryOrder</a></p>
<p class="sub-links-paragraph">    <a class="sub-links-action" href="../ONRSPQRYPARKEDORDER/">OnRspQryParkedOrder</a></p>
<p class="sub-links-paragraph">    <a class="sub-links-action" href="../ONRSPQRYPARKEDORDERACTION/">OnRspQryParkedOrderAction</a></p>
<p class="sub-links-paragraph">    <a class="sub-links-action" href="../ONRSPQRYPRODUCT/">OnRspQryProduct</a></p>
<p class="sub-links-paragraph">    <a class="sub-links-action" href="../ONRSPQRYPRODUCTEXCHRATE/">OnRspQryProductExchRate</a></p>
<p class="sub-links-paragraph">    <a class="sub-links-action" href="../ONRSPQRYPRODUCTGROUP/">OnRspQryProductGroup</a></p>
<p class="sub-links-paragraph">    <a class="sub-links-action" href="../ONRSPQRYQUOTE/">OnRspQryQuote</a></p>
<p class="sub-links-paragraph">    <a class="sub-links-action" href="../ONRSPQRYSECAGENTACIDMAP/">OnRspQrySecAgentACIDMap</a></p>
<p class="sub-links-paragraph">    <a class="sub-links-action" href="../ONRSPQRYSECAGENTCHECKMODE/">OnRspQrySecAgentCheckMode</a></p>
<p class="sub-links-paragraph">    <a class="sub-links-action" href="../ONRSPQRYSECAGENTTRADEINFO/">OnRspQrySecAgentTradeInfo</a></p>
<p class="sub-links-paragraph">    <a class="sub-links-action" href="../ONRSPQRYSECAGENTTRADINGACCOUNT/">OnRspQrySecAgentTradingAccount</a></p>
<p class="sub-links-paragraph">    <a class="sub-links-action" href="../ONRSPQRYSETTLEMENTINFO/">OnRspQrySettlementInfo</a></p>
<p class="sub-links-paragraph">    <a class="sub-links-action" href="../ONRSPQRYSETTLEMENTINFOCONFIRM/">OnRspQrySettlementInfoConfirm</a></p>
<p class="sub-links-paragraph">    <a class="sub-links-action" href="../ONRSPQRYTRADE/">OnRspQryTrade</a></p>
<p class="sub-links-paragraph">    <a class="sub-links-action" href="../ONRSPQRYTRADINGACCOUNT/">OnRspQryTradingAccount</a></p>
<p class="sub-links-paragraph">    <a class="sub-links-action" href="../ONRSPQRYTRADINGCODE/">OnRspQryTradingCode</a></p>
<p class="sub-links-paragraph">    <a class="sub-links-action" href="../ONRSPQRYTRADINGNOTICE/">OnRspQryTradingNotice</a></p>
<p class="sub-links-paragraph">    <a class="sub-links-action" href="../ONRSPQRYTRANSFERBANK/">OnRspQryTransferBank</a></p>
<p class="sub-links-paragraph">    <a class="sub-links-action" href="../ONRSPQRYTRANSFERSERIAL/">OnRspQryTransferSerial</a></p>
<p class="sub-links-paragraph">    <a class="sub-links-action" href="../ONRSPQUERYBANKACCOUNTMONEYBYFUTURE/">OnRspQueryBankAccountMoneyByFuture</a></p>
<p class="sub-links-paragraph">    <a class="sub-links-action" href="../ONRSPQUERYCFMMCTRADINGACCOUNTTOKEN/">OnRspQueryCFMMCTradingAccountToken</a></p>
<p class="sub-links-paragraph">    <a class="sub-links-action" href="../ONRSPQUOTEACTION/">OnRspQuoteAction</a></p>
<p class="sub-links-paragraph">    <a class="sub-links-action" href="../ONRSPQUOTEINSERT/">OnRspQuoteInsert</a></p>
<p class="sub-links-paragraph">    <a class="sub-links-action" href="../ONRSPREMOVEPARKEDORDER/">OnRspRemoveParkedOrder</a></p>
<p class="sub-links-paragraph">    <a class="sub-links-action" href="../ONRSPREMOVEPARKEDORDERACTION/">OnRspRemoveParkedOrderAction</a></p>
<p class="sub-links-paragraph">    <a class="sub-links-action" href="../ONRSPSETTLEMENTINFOCONFIRM/">OnRspSettlementInfoConfirm</a></p>
<p class="sub-links-paragraph">    <a class="sub-links-action" href="../ONRSPTRADINGACCOUNTPASSWORDUPDATE/">OnRspTradingAccountPasswordUpdate</a></p>
<p class="sub-links-paragraph">    <a class="sub-links-action" href="../ONRSPUSERAUTHMETHOD/">OnRspUserAuthMethod</a></p>
<p class="sub-links-paragraph">    <a class="sub-links-action" href="../ONRSPUSERLOGIN/">OnRspUserLogin</a></p>
<p class="sub-links-paragraph">    <a class="sub-links-action" href="../ONRSPUSERLOGOUT/">OnRspUserLogout</a></p>
<p class="sub-links-paragraph">    <a class="sub-links-action" href="../ONRSPUSERPASSWORDUPDATE/">OnRspUserPasswordUpdate</a></p>
<p class="sub-links-paragraph">    <a class="sub-links-action" href="../ONRTNBULLETIN/">OnRtnBulletin</a></p>
<p class="sub-links-paragraph">    <a class="sub-links-action" href="../ONRTNCANCELACCOUNTBYBANK/">OnRtnCancelAccountByBank</a></p>
<p class="sub-links-paragraph">    <a class="sub-links-action" href="../ONRTNCFMMCTRADINGACCOUNTTOKEN/">OnRtnCFMMCTradingAccountToken</a></p>
<p class="sub-links-paragraph">    <a class="sub-links-action" href="../ONRTNCHANGEACCOUNTBYBANK/">OnRtnChangeAccountByBank</a></p>
<p class="sub-links-paragraph">    <a class="sub-links-action" href="../ONRTNCOMBACTION/">OnRtnCombAction</a></p>
<p class="sub-links-paragraph">    <a class="sub-links-action" href="../ONRTNERRORCONDITIONALORDER/">OnRtnErrorConditionalOrder</a></p>
<p class="sub-links-paragraph">    <a class="sub-links-action" href="../ONRTNEXECORDER/">OnRtnExecOrder</a></p>
<p class="sub-links-paragraph">    <a class="sub-links-action" href="../ONRTNFORQUOTERSP/">OnRtnForQuoteRsp</a></p>
<p class="sub-links-paragraph">    <a class="sub-links-action" href="../ONRTNFROMBANKTOFUTUREBYBANK/">OnRtnFromBankToFutureByBank</a></p>
<p class="sub-links-paragraph">    <a class="sub-links-action" href="../ONRTNFROMBANKTOFUTUREBYFUTURE/">OnRtnFromBankToFutureByFuture</a></p>
<p class="sub-links-paragraph">    <a class="sub-links-action" href="../ONRTNFROMFUTURETOBANKBYBANK/">OnRtnFromFutureToBankByBank</a></p>
<p class="sub-links-paragraph">    <a class="sub-links-action" href="../ONRTNFROMFUTURETOBANKBYFUTURE/">OnRtnFromFutureToBankByFuture</a></p>
<p class="sub-links-paragraph">    <a class="sub-links-action" href="../ONRTNINSTRUMENTSTATUS/">OnRtnInstrumentStatus</a></p>
<p class="sub-links-paragraph">    <a class="sub-links-action" href="../ONRTNOPENACCOUNTBYBANK/">OnRtnOpenAccountByBank</a></p>
<p class="sub-links-paragraph">    <a class="sub-links-action" href="../ONRTNOPTIONSELFCLOSE/">OnRtnOptionSelfClose</a></p>
<p class="sub-links-paragraph">    <a class="sub-links-action" href="../ONRTNORDER/">OnRtnOrder</a></p>
<p class="sub-links-paragraph">    <a class="sub-links-action" href="../ONRTNQUERYBANKBALANCEBYFUTURE/">OnRtnQueryBankBalanceByFuture</a></p>
<p class="sub-links-paragraph">    <a class="sub-links-action" href="../ONRTNQUOTE/">OnRtnQuote</a></p>
<p class="sub-links-paragraph">    <a class="sub-links-action" href="../ONRTNREPEALFROMBANKTOFUTUREBYBANK/">OnRtnRepealFromBankToFutureByBank</a></p>
<p class="sub-links-paragraph">    <a class="sub-links-action" href="../ONRTNREPEALFROMBANKTOFUTUREBYFUTURE/">OnRtnRepealFromBankToFutureByFuture</a></p>
<p class="sub-links-paragraph">    <a class="sub-links-action" href="../ONRTNREPEALFROMBANKTOFUTUREBYFUTUREMANUAL/">OnRtnRepealFromBankToFutureByFutureManual</a></p>
<p class="sub-links-paragraph">    <a class="sub-links-action" href="../ONRTNREPEALFROMFUTURETOBANKBYBANK/">OnRtnRepealFromFutureToBankByBank</a></p>
<p class="sub-links-paragraph">    <a class="sub-links-action" href="../ONRTNREPEALFROMFUTURETOBANKBYFUTURE/">OnRtnRepealFromFutureToBankByFuture</a></p>
<p class="sub-links-paragraph">    <a class="sub-links-action" href="../ONRTNREPEALFROMFUTURETOBANKBYFUTUREMANUAL/">OnRtnRepealFromFutureToBankByFutureManual</a></p>
<p class="sub-links-paragraph">    <a class="sub-links-action" href="../ONRTNTRADE/">OnRtnTrade</a></p>
<p class="sub-links-paragraph">    <a class="sub-links-action" href="../ONRTNTRADINGNOTICE/">OnRtnTradingNotice</a></p>
<p class="sub-links-paragraph">    <a class="sub-links-action" href="../SM/">OnRspQueryMaxOrderVolume</a></p>
</div>
