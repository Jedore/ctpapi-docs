<p>期权自对冲操作请求响应，当执行<a href="../../CTHOSTFTDCTRADERSPI/REQOPTIONSELFCLOSEACTION/">ReqOptionSelfCloseAction</a>后，该方法被调用。</p>
<span class="anchor" id="28c4b2c0-46ef-4bac-8293-2467fc7ed087"></span>
## 1.函数原型
<p>virtual void OnRspOptionSelfCloseAction(CThostFtdcInputOptionSelfCloseActionField *pInputOptionSelfCloseAction, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="6d08fc15-e9ae-410f-b85b-9d02256f4e6d"></span>
## 2.参数
<p>pInputOptionSelfCloseAction：输入期权自对冲操作</p>
<pre><code>struct CThostFtdcInputOptionSelfCloseActionField
{
    ///经纪公司代码
    TThostFtdcBrokerIDType  BrokerID;
    ///投资者代码
    TThostFtdcInvestorIDType    InvestorID;
    ///期权自对冲操作引用
    TThostFtdcOrderActionRefType    OptionSelfCloseActionRef;
    ///期权自对冲引用
    TThostFtdcOrderRefType  OptionSelfCloseRef;
    ///请求编号
    TThostFtdcRequestIDType RequestID;
    ///前置编号
    TThostFtdcFrontIDType   FrontID;
    ///会话编号
    TThostFtdcSessionIDType SessionID;
    ///交易所代码
    TThostFtdcExchangeIDType    ExchangeID;
    ///期权自对冲操作编号
    TThostFtdcOrderSysIDType    OptionSelfCloseSysID;
    ///操作标志
    TThostFtdcActionFlagType    ActionFlag;
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
<p>ActionFlag：只有删除标志，修改标志位不支持</p>
<p>InstallID：CTP内部使用</p>
<p>StatusMsg：报错信息</p>
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
<span class="anchor" id="73eab4c1-cf0d-48d7-af1d-4c77c2cb4998"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="a87f7440-4a8f-45d5-8705-449830f30297"></span>
## 4.FAQ
<p>无</p>
