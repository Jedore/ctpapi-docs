<p>期权自对冲操作请求响应，当执行<a href="../../CTHOSTFTDCTRADERSPI/REQOPTIONSELFCLOSEACTION/">ReqOptionSelfCloseAction</a>后，该方法被调用。</p>
<span class="anchor" id="6d5535e9-b5d8-4610-8d85-4eb23dcba09d"></span>
## 1.函数原型
<p>virtual void OnRspOptionSelfCloseAction(CThostFtdcInputOptionSelfCloseActionField *pInputOptionSelfCloseAction, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="dbfe78eb-b46b-420a-ad17-13c85bb1b378"></span>
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
<span class="anchor" id="d7ad6ea5-2da6-4f72-9846-518ae2ee1bbd"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="5ef355a1-d859-42c6-b307-152286c73627"></span>
## 4.FAQ
<p>无</p>
