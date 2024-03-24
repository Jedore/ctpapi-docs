<p>报单操作请求响应，当执行ReqOrderAction后有字段填写不对之类的CTP报错则通过此接口返回</p>
<span class="anchor" id="8ec78a7e-4c10-4551-8838-8136d8592fbb"></span>
## 1.函数原型
<p>virtual void OnRspOrderAction(CThostFtdcInputOrderActionField *pInputOrderAction, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="5636497d-6964-4224-b102-3a59fe29e126"></span>
## 2.参数
<p>pInputOrderAction：输入报单操作</p>
<pre><code>struct CThostFtdcInputOrderActionField
{
    ///经纪公司代码
    TThostFtdcBrokerIDType BrokerID;
    ///投资者代码
    TThostFtdcInvestorIDType InvestorID;
    ///报单操作引用
    TThostFtdcOrderActionRefType OrderActionRef;
    ///报单引用
    TThostFtdcOrderRefType OrderRef;
    ///请求编号
    TThostFtdcRequestIDType RequestID;
    ///前置编号
    TThostFtdcFrontIDType FrontID;
    ///会话编号
    TThostFtdcSessionIDType SessionID;
    ///交易所代码
    TThostFtdcExchangeIDType ExchangeID;
    ///报单编号
    TThostFtdcOrderSysIDType OrderSysID;
    ///操作标志
    TThostFtdcActionFlagType ActionFlag;
    ///价格
    TThostFtdcPriceType LimitPrice;
    ///数量变化
    TThostFtdcVolumeType VolumeChange;
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
<span class="anchor" id="7cdede8a-3632-4256-8f65-9ed105c05bf3"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="a13d0a36-a6ec-4f86-a995-4b9de38977ac"></span>
## 4.FAQ
<p>无</p>
