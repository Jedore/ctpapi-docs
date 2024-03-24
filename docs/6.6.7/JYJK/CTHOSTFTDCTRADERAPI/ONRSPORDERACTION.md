<p>报单操作请求响应，当执行<a href="../../CTHOSTFTDCTRADERSPI/REQORDERACTION/">ReqOrderAction</a>后有字段填写不对之类的CTP报错则通过此接口返回</p>
<span class="anchor" id="40a1becd-2ee9-40df-9173-e7ef4ce35cf6"></span>
## 1.函数原型
<p>virtual void OnRspOrderAction(CThostFtdcInputOrderActionField *pInputOrderAction, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="e0384e24-e322-4a63-8412-4dbf00c2cf09"></span>
## 2.参数
<p>pInputOrderAction：输入报单操作</p>
<pre><code>struct CThostFtdcInputOrderActionField
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
<p>ActionFlag：目前只有删除（撤单）的操作，修改（改单）的操作还没有，可以通过撤单之后重新报单实现。</p>
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
<span class="anchor" id="eeb87528-afe6-497b-82de-75b1deb0f33b"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="61f289b7-de7f-4c91-a3e1-6cfcdcf7b829"></span>
## 4.FAQ
<p>无</p>
