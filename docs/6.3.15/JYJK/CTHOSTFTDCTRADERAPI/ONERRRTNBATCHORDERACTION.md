<p>批量报单操作错误回报</p>
<span class="anchor" id="5acd09ef-df16-4a7d-9f50-5fe6468b3f0c"></span>
## 1.函数原型
<p>virtual void OnErrRtnBatchOrderAction(CThostFtdcBatchOrderActionField *pBatchOrderAction, CThostFtdcRspInfoField *pRspInfo) {};</p>
<span class="anchor" id="32e2ff76-cdce-4808-a047-9d0df1309e70"></span>
## 2.参数
<p>pBatchOrderAction：批量报单操作</p>
<pre><code>struct CThostFtdcBatchOrderActionField
{
    ///经纪公司代码
    TThostFtdcBrokerIDType BrokerID;
    ///投资者代码
    TThostFtdcInvestorIDType InvestorID;
    ///报单操作引用
    TThostFtdcOrderActionRefType OrderActionRef;
    ///请求编号
    TThostFtdcRequestIDType RequestID;
    ///前置编号
    TThostFtdcFrontIDType FrontID;
    ///会话编号
    TThostFtdcSessionIDType SessionID;
    ///交易所代码
    TThostFtdcExchangeIDType ExchangeID;
    ///操作日期
    TThostFtdcDateType ActionDate;
    ///操作时间
    TThostFtdcTimeType ActionTime;
    ///交易所交易员代码
    TThostFtdcTraderIDType TraderID;
    ///安装编号
    TThostFtdcInstallIDType InstallID;
    ///操作本地编号
    TThostFtdcOrderLocalIDType ActionLocalID;
    ///会员代码
    TThostFtdcParticipantIDType ParticipantID;
    ///客户代码
    TThostFtdcClientIDType ClientID;
    ///业务单元
    TThostFtdcBusinessUnitType BusinessUnit;
    ///报单操作状态
    TThostFtdcOrderActionStatusType OrderActionStatus;
    ///用户代码
    TThostFtdcUserIDType UserID;
    ///状态信息
    TThostFtdcErrorMsgType StatusMsg;
    ///投资单元代码
    TThostFtdcInvestUnitIDType InvestUnitID;
    ///IP地址
    TThostFtdcIPAddressType IPAddress;
    ///Mac地址
    TThostFtdcMacAddressType MacAddress;
};
</code></pre>
<p>OrderActionStatus：撤单后报单的状态</p>
<p>StatusMsg：撤单错误的状态信息，如果没有错误的则返回0</p>
<p>pRspInfo：响应信息</p>
<pre><code>struct CThostFtdcRspInfoField
{
    ///错误代码
    TThostFtdcErrorIDType ErrorID;
    ///错误信息
    TThostFtdcErrorMsgType ErrorMsg;
};
</code></pre>
<span class="anchor" id="6f03de4f-70b8-4c26-97fd-d97c0af603b5"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="802f33b4-f318-45cd-912d-7277f06cf439"></span>
## 4.FAQ
<p>无</p>
