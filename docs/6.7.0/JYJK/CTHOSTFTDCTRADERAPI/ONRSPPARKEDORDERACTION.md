<p>预埋撤单录入请求响应，当执行<a href="../../CTHOSTFTDCTRADERSPI/REQPARKEDORDERACTION/">ReqParkedOrderAction</a>后，该方法被调用</p>
<span class="anchor" id="8a1415e3-0016-471d-80cd-4ad3624e1cbf"></span>
## 1.函数原型
<p>virtual void OnRspParkedOrderAction(CThostFtdcParkedOrderActionField *pParkedOrderAction, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="a4907ae3-459d-4ecd-89f6-ecaace7ddac5"></span>
## 2.参数
<p>pParkedOrderAction：输入预埋单操作</p>
<pre><code>struct CThostFtdcParkedOrderActionField
{
    ///经纪公司代码
    TThostFtdcBrokerIDType  BrokerID;
    ///投资者代码
    TThostFtdcInvestorIDType    InvestorID;
    ///报单操作引用
    TThostFtdcOrderActionRefType    OrderActionRef;
    ///报单引用
    TThostFtdcOrderRefType  OrderRef;
    ///请求编号
    TThostFtdcRequestIDType RequestID;
    ///前置编号
    TThostFtdcFrontIDType   FrontID;
    ///会话编号
    TThostFtdcSessionIDType SessionID;
    ///交易所代码
    TThostFtdcExchangeIDType    ExchangeID;
    ///报单编号
    TThostFtdcOrderSysIDType    OrderSysID;
    ///操作标志
    TThostFtdcActionFlagType    ActionFlag;
    ///价格
    TThostFtdcPriceType LimitPrice;
    ///数量变化
    TThostFtdcVolumeType    VolumeChange;
    ///用户代码
    TThostFtdcUserIDType    UserID;
    ///保留的无效字段
    TThostFtdcOldInstrumentIDType   reserve1;
    ///预埋撤单单编号
    TThostFtdcParkedOrderActionIDType   ParkedOrderActionID;
    ///用户类型
    TThostFtdcUserTypeType  UserType;
    ///预埋撤单状态
    TThostFtdcParkedOrderStatusType Status;
    ///错误代码
    TThostFtdcErrorIDType   ErrorID;
    ///错误信息
    TThostFtdcErrorMsgType  ErrorMsg;
    ///投资单元代码
    TThostFtdcInvestUnitIDType  InvestUnitID;
    ///保留的无效字段
    TThostFtdcOldIPAddressType  reserve2;
    ///Mac地址
    TThostFtdcMacAddressType    MacAddress;
    ///合约代码
    TThostFtdcInstrumentIDType  InstrumentID;
    ///IP地址
    TThostFtdcIPAddressType IPAddress;
};
</code></pre>
<p>Status：预埋单的最后情况</p>
<p>pRspInfo：响应信息</p>
<pre><code>struct CThostFtdcRspInfoField
{
    ///错误代码
    TThostFtdcErrorIDType ErrorID;
    ///错误信息
    TThostFtdcErrorMsgType ErrorMsg;
};
</code></pre>
<p>nRequestID：返回用户操作请求的ID，该ID 由用户在操作请求时指定。</p>
<p>bIsLast：指示该次返回是否为针对nRequestID的最后一次返回。</p>
<span class="anchor" id="72418012-f69e-4d8a-80a9-8793900c8866"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="aa38656b-087e-40df-b14d-d2cf25407dee"></span>
## 4.FAQ
<p>无</p>
