<p>报单操作请求响应，当执行<a href="../../CTHOSTFTDCTRADERSPI/REQORDERACTION/">ReqOrderAction</a>后有字段填写不对之类的CTP报错则通过此接口返回</p>
<span class="anchor" id="e344e726-8e6e-49ec-ac37-c64f85ee0c8e"></span>
## 1.函数原型
<p>virtual void OnRspOrderAction(CThostFtdcInputOrderActionField *pInputOrderAction, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="e6845164-bcb0-43dc-8354-b0e23142d488"></span>
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
    ///报单回显字段
    TThostFtdcOrderMemoType OrderMemo;
    ///session上请求计数 api自动维护
    TThostFtdcSequenceNo12Type  SessionReqSeq;
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
<span class="anchor" id="71aa8e7f-c82e-415d-8e6f-b860397a91a5"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="ca767d5f-3c3a-48dc-a237-a45d1896c6eb"></span>
## 4.FAQ
<p>无</p>
