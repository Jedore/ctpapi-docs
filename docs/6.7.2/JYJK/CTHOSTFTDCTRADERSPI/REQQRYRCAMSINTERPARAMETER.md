<p>请求RCAMS跨品种风险折抵参数查询，对应响应请求<a href="../../CTHOSTFTDCTRADERAPI/ONRSPQRYRCAMSINTERPARAMETER/">OnRspQryRCAMSInterParameter</a></p>
<span class="anchor" id="2e4d88a1-93ce-45e5-af87-d07738cc51e7"></span>
## 1.函数原型
<p>virtual int ReqQryRCAMSInterParameter(CThostFtdcQryRCAMSInterParameterField *pQryRCAMSInterParameter, int nRequestID) = 0;</p>
<span class="anchor" id="e7557e91-2f74-4203-b65d-d3eae1b5b422"></span>
## 2.参数
<p>pQryRCAMSInterParameter：RCAMS跨品种风险折抵参数查询</p>
<table><tr><th style="TEXT-ALIGN: center;">字段类型</th><th style="TEXT-ALIGN: center;">字段名称</th><th style="TEXT-ALIGN: center;">含义</th><th style="TEXT-ALIGN: center;">是否可作为过滤条件</th></tr><tr><td style="TEXT-ALIGN: left;">TThostFtdcProductIDType</td>
<td style="TEXT-ALIGN: left;">ProductGroupID</td>
<td style="TEXT-ALIGN: left;">商品群代码</td>
<td style="TEXT-ALIGN: left;"><strong><font color="#FF0000">是</font></strong></td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcProductIDType</td>
<td style="TEXT-ALIGN: left;">CombProduct1</td>
<td style="TEXT-ALIGN: left;">产品组合代码1</td>
<td style="TEXT-ALIGN: left;"><strong><font color="#FF0000">是</font></strong></td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcProductIDType</td>
<td style="TEXT-ALIGN: left;">CombProduct2</td>
<td style="TEXT-ALIGN: left;">产品组合代码2</td>
<td style="TEXT-ALIGN: left;"><strong><font color="#FF0000">是</font></strong></td>
</tr>
</table>
<span class="anchor" id="eaac72f5-fd7a-4d36-9707-53e57627b71e"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="659b8a93-df2e-4133-942f-f7ee77998cd9"></span>
## 4.调用示例
<p>无</p>
<span class="anchor" id="d03b71fd-0bdc-4060-bce1-cdc43c6c4059"></span>
## 5.FAQ
<p>无</p>
