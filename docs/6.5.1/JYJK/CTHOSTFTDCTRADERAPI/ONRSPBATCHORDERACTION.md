<p>批量报单操作请求响应，当执行ReqBatchOrderAction后有字段填写不对之类的CTP报错则通过此接口返回</p>
<span class="anchor" id="565ab74a-4e87-44f8-807c-e8ea46414032"></span>
## 1.函数原型
<p>virtual void OnRspBatchOrderAction(CThostFtdcInputBatchOrderActionField *pInputBatchOrderAction, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="7a5b87ab-be92-41ab-ba9c-6a075a6ed767"></span>
## 2.参数
<p>pInputBatchOrderAction：输入批量报单操作</p>
<pre><code>struct CThostFtdcInputBatchOrderActionField
{
    ///经纪公司代码
    TThostFtdcBrokerIDType  BrokerID;
    ///投资者代码
    TThostFtdcInvestorIDType    InvestorID;
    ///报单操作引用
    TThostFtdcOrderActionRefType    OrderActionRef;
    ///请求编号
    TThostFtdcRequestIDType RequestID;
    ///前置编号
    TThostFtdcFrontIDType   FrontID;
    ///会话编号
    TThostFtdcSessionIDType SessionID;
    ///交易所代码
    TThostFtdcExchangeIDType    ExchangeID;
    ///用户代码
    TThostFtdcUserIDType    UserID;
    ///投资单元代码
    TThostFtdcInvestUnitIDType  InvestUnitID;
    ///保留的无效字段
    TThostFtdcOldIPAddressType  reserve1;
    ///Mac地址
    TThostFtdcMacAddressType    MacAddress;
    ///IP地址
    TThostFtdcIPAddressType IPAddress;
};
</code></pre>
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
<span class="anchor" id="f837c2c5-55c6-4daf-b60c-5146dc8265ff"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="e440c255-037f-4cfb-8c89-0136dbed22b3"></span>
## 4.FAQ
<p>无</p>
