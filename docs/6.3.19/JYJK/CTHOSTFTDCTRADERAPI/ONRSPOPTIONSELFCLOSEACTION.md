<p>期权自对冲操作请求响应，当执行ReqOptionSelfCloseAction后，该方法被调用。</p>
<span class="anchor" id="0f2e734d-57b3-44e4-a9df-e12e7920d717"></span>
## 1.函数原型
<p>virtual void OnRspOptionSelfCloseAction(CThostFtdcInputOptionSelfCloseActionField *pInputOptionSelfCloseAction, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="7c64bd01-af96-4a39-8b4a-7a60fc6e4bc1"></span>
## 2.参数
<p>pInputOptionSelfCloseAction：输入期权自对冲操作</p>
<pre><code>struct CThostFtdcInputOptionSelfCloseActionField
{
    ///经纪公司代码
    TThostFtdcBrokerIDType BrokerID;
    ///投资者代码
    TThostFtdcInvestorIDType InvestorID;
    ///期权自对冲操作引用
    TThostFtdcOrderActionRefType OptionSelfCloseActionRef;
    ///期权自对冲引用
    TThostFtdcOrderRefType OptionSelfCloseRef;
    ///请求编号
    TThostFtdcRequestIDType RequestID;
    ///前置编号
    TThostFtdcFrontIDType FrontID;
    ///会话编号
    TThostFtdcSessionIDType SessionID;
    ///交易所代码
    TThostFtdcExchangeIDType ExchangeID;
    ///期权自对冲操作编号
    TThostFtdcOrderSysIDType OptionSelfCloseSysID;
    ///操作标志
    TThostFtdcActionFlagType ActionFlag;
    ///用户代码
    TThostFtdcUserIDType UserID;
    ///合约代码
    TThostFtdcInstrumentIDType InstrumentID;
    ///投资单元代码
    TThostFtdcInvestUnitIDType InvestUnitID;
    ///IP地址
    TThostFtdcIPAddressType IPAddress;
    ///Mac地址
    TThostFtdcMacAddressType MacAddress;
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
<span class="anchor" id="07818395-7a34-4c60-9e00-35d04019c2a7"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="d3b378fd-31d9-4cab-a2d4-68af0f787dbb"></span>
## 4.FAQ
<p>无</p>
